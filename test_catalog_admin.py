import hashlib
import json
from types import SimpleNamespace
from urllib.error import HTTPError

import pytest

import catalog_admin


def _image(url="https://images.example.com/photo.jpg", title="Photo"):
    return {
        "url": url,
        "title": title,
        "description": "Catalog image",
        "icon": "🖼️",
        "public_id": "",
    }


def test_manifest_applies_overrides_and_keeps_new_service_defaults():
    defaults = {"office-lan": [_image()], "new-service": [_image(title="Default")]}
    stored = {"office-lan": [_image("https://res.cloudinary.com/demo/image/upload/lan.jpg")]}

    merged = catalog_admin.merge_catalog_manifest(defaults, stored)

    assert merged["office-lan"][0]["url"].endswith("lan.jpg")
    assert merged["new-service"][0]["title"] == "Default"


def test_manifest_rejects_service_with_no_images():
    with pytest.raises(catalog_admin.CatalogStorageError, match="at least one image"):
        catalog_admin.merge_catalog_manifest({"office-lan": [_image()]}, {"office-lan": []})


def test_image_upload_checks_type_and_size():
    unsupported = SimpleNamespace(type="text/plain", getvalue=lambda: b"bad")
    oversized = SimpleNamespace(
        type="image/jpeg",
        getvalue=lambda: b"x" * (catalog_admin.MAX_IMAGE_BYTES + 1),
    )

    with pytest.raises(catalog_admin.CatalogStorageError, match="JPEG, PNG, or WebP"):
        catalog_admin.validate_image_upload(unsupported)
    with pytest.raises(catalog_admin.CatalogStorageError, match="10 MB"):
        catalog_admin.validate_image_upload(oversized)


def test_otp_verification_accepts_only_matching_ascii_six_digit_code():
    expected_hash = hashlib.sha256(b"123456").hexdigest()

    assert catalog_admin.verify_otp_code("123456", expected_hash)
    assert not catalog_admin.verify_otp_code("123457", expected_hash)
    assert not catalog_admin.verify_otp_code("１２３４５６", expected_hash)


def test_brevo_otp_is_sent_only_to_configured_admin(monkeypatch):
    sent = {}

    class Response:
        status = 201

        def __enter__(self):
            return self

        def __exit__(self, *_):
            return False

    def fake_urlopen(request, timeout):
        sent["request"] = request
        sent["timeout"] = timeout
        return Response()

    monkeypatch.setattr(
        catalog_admin,
        "_brevo_settings",
        lambda: {"api_key": "test-key", "sender_email": "sender@example.com"},
    )
    monkeypatch.setattr(catalog_admin, "urlopen", fake_urlopen)

    catalog_admin._send_otp_email("123456")

    request = sent["request"]
    payload = json.loads(request.data)
    assert request.full_url == "https://api.brevo.com/v3/smtp/email"
    assert payload["to"] == [{"email": catalog_admin.ADMIN_EMAIL}]
    assert "123456" in payload["textContent"]
    assert sent["timeout"] == 10


def test_brevo_401_error_identifies_api_key_problem(monkeypatch):
    monkeypatch.setattr(
        catalog_admin,
        "_brevo_settings",
        lambda: {"api_key": "test-key", "sender_email": "sender@example.com"},
    )

    def reject_request(request, timeout):
        raise HTTPError(request.full_url, 401, "Unauthorized", None, None)

    monkeypatch.setattr(catalog_admin, "urlopen", reject_request)

    with pytest.raises(catalog_admin.AdminAuthenticationError, match="API key is invalid"):
        catalog_admin._send_otp_email("123456")
