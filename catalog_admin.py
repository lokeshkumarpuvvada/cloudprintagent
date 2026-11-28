import copy
import hashlib
import hmac
import io
import json
import re
import secrets
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen

import cloudinary
import cloudinary.uploader
import streamlit as st
from streamlit.errors import StreamlitSecretNotFoundError

ADMIN_EMAIL = "1432@gmail.com"
DEFAULT_SENDER_EMAIL = "hanvikaits@gmail.com"
MANIFEST_PUBLIC_ID = "hanvika/catalog-manifest.json"
MAX_IMAGE_BYTES = 10 * 1024 * 1024
ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/webp"}
OTP_EXPIRY_SECONDS = 5 * 60
OTP_RESEND_SECONDS = 60
OTP_MAX_SENDS_PER_WINDOW = 3
OTP_WINDOW_SECONDS = 15 * 60
OTP_MAX_ATTEMPTS = 5
OTP_LOCKOUT_SECONDS = 15 * 60
ADMIN_SESSION_SECONDS = 30 * 60


class CatalogStorageError(RuntimeError):
    pass


class AdminAuthenticationError(RuntimeError):
    pass


def _secret(section, key, flat_name):
    try:
        nested = st.secrets.get(section, {})
        value = nested.get(key) if hasattr(nested, "get") else None
        if value is None:
            value = st.secrets.get(flat_name)
    except StreamlitSecretNotFoundError:
        return ""
    if value is None:
        return ""
    return str(value).strip()


def _cloudinary_settings():
    return {
        "cloud_name": _secret("cloudinary", "cloud_name", "CLOUDINARY_CLOUD_NAME"),
        "api_key": _secret("cloudinary", "api_key", "CLOUDINARY_API_KEY"),
        "api_secret": _secret("cloudinary", "api_secret", "CLOUDINARY_API_SECRET"),
    }


def _brevo_settings():
    return {
        "api_key": _secret("brevo", "api_key", "BREVO_API_KEY"),
        "sender_email": _secret("brevo", "sender_email", "BREVO_SENDER_EMAIL")
        or DEFAULT_SENDER_EMAIL,
    }


def _configure_cloudinary():
    settings = _cloudinary_settings()
    if not all(settings.values()):
        raise CatalogStorageError(
            "Cloudinary secrets are missing. Add cloud_name, api_key, and api_secret."
        )
    cloudinary.config(**settings, secure=True)
    return settings


def _manifest_url(cloud_name):
    public_id = quote(MANIFEST_PUBLIC_ID, safe="/")
    return f"https://res.cloudinary.com/{quote(cloud_name, safe='')}/raw/upload/{public_id}"


def _validate_item(item):
    if not isinstance(item, dict):
        raise CatalogStorageError("A catalog image entry is not a valid object.")
    url = item.get("url")
    title = item.get("title")
    description = item.get("description", "")
    icon = item.get("icon", "🖼️")
    public_id = item.get("public_id", "")
    if not all(isinstance(value, str) for value in (url, title, description, icon, public_id)):
        raise CatalogStorageError("Catalog image fields must be text.")
    parsed_url = urlparse(url)
    if parsed_url.scheme != "https" or not parsed_url.netloc:
        raise CatalogStorageError("Catalog image URLs must use HTTPS.")
    if not title.strip() or len(title) > 120 or len(description) > 500:
        raise CatalogStorageError("Catalog image titles or descriptions are invalid.")
    if len(icon) > 8 or len(public_id) > 250:
        raise CatalogStorageError("Catalog image metadata is too long.")
    return {
        "url": url,
        "title": title.strip(),
        "description": description.strip(),
        "icon": icon,
        "public_id": public_id,
    }


def merge_catalog_manifest(default_catalog, stored_catalog):
    if not isinstance(stored_catalog, dict):
        raise CatalogStorageError("The saved service catalog has an invalid format.")
    result = copy.deepcopy(default_catalog)
    for service_id in result:
        if service_id not in stored_catalog:
            continue
        items = stored_catalog[service_id]
        if not isinstance(items, list) or not items:
            raise CatalogStorageError(
                f"The saved catalog for {service_id} must contain at least one image."
            )
        result[service_id] = [_validate_item(item) for item in items]
    return result


def load_service_catalog(default_catalog):
    settings = _cloudinary_settings()
    if not all(settings.values()):
        return copy.deepcopy(default_catalog)
    cloudinary.config(**settings, secure=True)
    request = Request(
        _manifest_url(settings["cloud_name"]),
        headers={"Accept": "application/json"},
    )
    try:
        with urlopen(request, timeout=8) as response:
            manifest = json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        if error.code == 404:
            return copy.deepcopy(default_catalog)
        raise CatalogStorageError(
            f"Cloudinary could not load the catalog (HTTP {error.code})."
        ) from error
    except URLError as error:
        raise CatalogStorageError("Could not reach Cloudinary to load the catalog.") from error
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise CatalogStorageError("Cloudinary returned an unreadable catalog manifest.") from error
    if not isinstance(manifest, dict) or manifest.get("version") != 1:
        raise CatalogStorageError("The saved service catalog version is not supported.")
    return merge_catalog_manifest(default_catalog, manifest.get("services"))


def _validate_complete_catalog(catalog):
    if not isinstance(catalog, dict) or not catalog:
        raise CatalogStorageError("The service catalog is empty or invalid.")
    normalized = {}
    for service_id, items in catalog.items():
        if not isinstance(service_id, str) or not isinstance(items, list) or not items:
            raise CatalogStorageError("Every service must keep at least one catalog image.")
        normalized[service_id] = [_validate_item(item) for item in items]
    return normalized


def save_service_catalog(catalog):
    settings = _configure_cloudinary()
    normalized = _validate_complete_catalog(catalog)
    manifest = json.dumps(
        {"version": 1, "services": normalized},
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    stream = io.BytesIO(manifest)
    stream.name = "catalog-manifest.json"
    try:
        result = cloudinary.uploader.upload(
            stream,
            resource_type="raw",
            public_id=MANIFEST_PUBLIC_ID,
            overwrite=True,
            invalidate=True,
        )
    except cloudinary.exceptions.Error as error:
        raise CatalogStorageError(
            "Cloudinary could not save the image catalog. Check the API credentials and quota."
        ) from error
    if not result.get("secure_url"):
        raise CatalogStorageError("Cloudinary did not confirm the catalog save.")


def validate_image_upload(uploaded_file):
    if uploaded_file is None:
        raise CatalogStorageError("Choose an image file first.")
    if uploaded_file.type not in ALLOWED_IMAGE_TYPES:
        raise CatalogStorageError("Upload a JPEG, PNG, or WebP image.")
    data = uploaded_file.getvalue()
    if not data or len(data) > MAX_IMAGE_BYTES:
        raise CatalogStorageError("Image files must be between 1 byte and 10 MB.")
    return data


def upload_catalog_image(service_id, uploaded_file):
    data = validate_image_upload(uploaded_file)
    _configure_cloudinary()
    stream = io.BytesIO(data)
    stream.name = uploaded_file.name
    try:
        result = cloudinary.uploader.upload(
            stream,
            resource_type="image",
            folder=f"hanvika/catalog/{service_id}",
            unique_filename=True,
            overwrite=False,
            use_filename=False,
            invalidate=True,
        )
    except cloudinary.exceptions.Error as error:
        raise CatalogStorageError(
            "Cloudinary could not upload the image. Check the account and storage quota."
        ) from error
    secure_url = result.get("secure_url", "")
    public_id = result.get("public_id", "")
    if not secure_url or not public_id:
        raise CatalogStorageError("Cloudinary did not confirm the image upload.")
    return {"url": secure_url, "public_id": public_id}


def _otp_digest(code):
    return hashlib.sha256(code.encode("ascii")).hexdigest()


def verify_otp_code(code, expected_hash):
    return bool(re.fullmatch(r"[0-9]{6}", code)) and hmac.compare_digest(
        _otp_digest(code), expected_hash
    )


def _send_otp_email(code):
    settings = _brevo_settings()
    if not settings["api_key"] or not settings["sender_email"]:
        raise AdminAuthenticationError("Brevo API key or verified sender email is missing.")
    payload = json.dumps(
        {
            "sender": {"name": "Hanvika IT Solutions", "email": settings["sender_email"]},
            "to": [{"email": ADMIN_EMAIL}],
            "subject": "Hanvika admin sign-in code",
            "textContent": (
                f"Your Hanvika admin sign-in code is {code}. "
                "It expires in 5 minutes. Do not share this code with anyone."
            ),
        }
    ).encode("utf-8")
    request = Request(
        "https://api.brevo.com/v3/smtp/email",
        data=payload,
        headers={
            "accept": "application/json",
            "api-key": settings["api_key"],
            "content-type": "application/json",
        },
        method="POST",
    )
    try:
        with urlopen(request, timeout=10) as response:
            if response.status < 200 or response.status >= 300:
                raise AdminAuthenticationError(
                    f"Brevo rejected the OTP email (HTTP {response.status})."
                )
    except HTTPError as error:
        raise AdminAuthenticationError(
            f"Brevo rejected the OTP email (HTTP {error.code}); check sender verification."
        ) from error
    except URLError as error:
        raise AdminAuthenticationError("Could not reach Brevo to send the OTP email.") from error


def _request_otp():
    now = time.time()
    state = st.session_state
    if now < state.get("admin_otp_lockout_until", 0):
        raise AdminAuthenticationError("Too many incorrect codes. Try again after 15 minutes.")
    sent_times = [
        sent_at
        for sent_at in state.get("admin_otp_sent_times", [])
        if now - sent_at < OTP_WINDOW_SECONDS
    ]
    if len(sent_times) >= OTP_MAX_SENDS_PER_WINDOW:
        raise AdminAuthenticationError("OTP send limit reached. Try again after 15 minutes.")
    if sent_times and now - sent_times[-1] < OTP_RESEND_SECONDS:
        raise AdminAuthenticationError("Wait 60 seconds before requesting another OTP.")
    code = f"{secrets.randbelow(1_000_000):06d}"
    _send_otp_email(code)
    sent_times.append(now)
    state["admin_otp_sent_times"] = sent_times
    state["admin_otp_hash"] = _otp_digest(code)
    state["admin_otp_expires_at"] = now + OTP_EXPIRY_SECONDS
    state["admin_otp_attempts"] = 0


def _verify_otp(code):
    now = time.time()
    state = st.session_state
    if now < state.get("admin_otp_lockout_until", 0):
        raise AdminAuthenticationError("Too many incorrect codes. Try again after 15 minutes.")
    expected_hash = state.get("admin_otp_hash")
    if not expected_hash or now >= state.get("admin_otp_expires_at", 0):
        state.pop("admin_otp_hash", None)
        raise AdminAuthenticationError("The OTP is missing or expired. Request a new one.")
    if not verify_otp_code(code, expected_hash):
        attempts = state.get("admin_otp_attempts", 0) + 1
        state["admin_otp_attempts"] = attempts
        if attempts >= OTP_MAX_ATTEMPTS:
            state["admin_otp_lockout_until"] = now + OTP_LOCKOUT_SECONDS
            state.pop("admin_otp_hash", None)
            raise AdminAuthenticationError("Too many incorrect codes. Try again after 15 minutes.")
        raise AdminAuthenticationError("The OTP is incorrect.")
    state.pop("admin_otp_hash", None)
    state["admin_authenticated_until"] = now + ADMIN_SESSION_SECONDS


def _persist_catalog(catalog):
    try:
        save_service_catalog(catalog)
    except CatalogStorageError as error:
        st.error(str(error))
        return False
    st.session_state["catalog_admin_notice"] = "Service images saved to Cloudinary."
    st.rerun()
    return True


def render_admin_panel(catalog, service_names):
    st.title("Service Image Admin")
    st.caption("Admin access is restricted to the verified OTP email account.")

    cloudinary_settings = _cloudinary_settings()
    brevo_settings = _brevo_settings()
    if not all(cloudinary_settings.values()):
        st.error("Cloudinary setup is incomplete. Check the required Streamlit Secrets keys.")
        return
    if not brevo_settings["api_key"]:
        st.error("Brevo API key is missing from Streamlit Secrets.")
        return

    authenticated_until = st.session_state.get("admin_authenticated_until", 0)
    if authenticated_until and time.time() >= authenticated_until:
        st.session_state.pop("admin_authenticated_until", None)
        st.info("Your admin session expired. Request a new OTP.")
        authenticated_until = 0

    if not authenticated_until:
        st.info(f"An OTP will be sent only to {ADMIN_EMAIL}.")
        if st.button("Send sign-in OTP", type="primary", key="admin_send_otp"):
            try:
                _request_otp()
            except AdminAuthenticationError as error:
                st.error(str(error))
            else:
                st.success("OTP sent. Check the admin email inbox.")
        if st.session_state.get("admin_otp_hash"):
            with st.form("admin_verify_otp"):
                otp = st.text_input("Six-digit OTP", max_chars=6, type="password")
                submitted = st.form_submit_button("Verify and open admin panel")
            if submitted:
                try:
                    _verify_otp(otp.strip())
                except AdminAuthenticationError as error:
                    st.error(str(error))
                else:
                    st.rerun()
        return

    if st.button("Sign out", key="admin_sign_out"):
        for key in tuple(st.session_state):
            if key.startswith("admin_"):
                st.session_state.pop(key, None)
        st.rerun()

    notice = st.session_state.pop("catalog_admin_notice", None)
    if notice:
        st.success(notice)

    service_id = st.selectbox(
        "Choose a service",
        list(service_names),
        format_func=lambda value: service_names[value],
    )
    items = catalog[service_id]
    st.caption("At least one image must remain in every service catalog.")

    for index, item in enumerate(items):
        with st.container(border=True):
            st.image(item["url"], width=280)
            title = st.text_input(
                "Image title",
                value=item["title"],
                key=f"catalog-title-{service_id}-{index}",
                max_chars=120,
            )
            description = st.text_area(
                "Image description",
                value=item["description"],
                key=f"catalog-description-{service_id}-{index}",
                max_chars=500,
            )
            uploaded_file = st.file_uploader(
                "Replace this image",
                type=["jpg", "jpeg", "png", "webp"],
                max_upload_size=10,
                key=f"catalog-replace-{service_id}-{index}",
            )
            save_col, replace_col, remove_col = st.columns(3)
            with save_col:
                save_text = st.button("Save text", key=f"catalog-save-text-{service_id}-{index}")
            with replace_col:
                replace_image = st.button("Replace image", key=f"catalog-replace-button-{service_id}-{index}")
            with remove_col:
                remove_image = st.button(
                    "Remove image",
                    key=f"catalog-remove-{service_id}-{index}",
                    disabled=len(items) == 1,
                )

            if save_text:
                updated_catalog = copy.deepcopy(catalog)
                updated_catalog[service_id][index]["title"] = title.strip()
                updated_catalog[service_id][index]["description"] = description.strip()
                _persist_catalog(updated_catalog)
            elif replace_image:
                if uploaded_file is None:
                    st.error("Choose a replacement image first.")
                else:
                    try:
                        uploaded = upload_catalog_image(service_id, uploaded_file)
                        updated_catalog = copy.deepcopy(catalog)
                        updated_catalog[service_id][index].update(uploaded)
                        _persist_catalog(updated_catalog)
                    except CatalogStorageError as error:
                        st.error(str(error))
            elif remove_image:
                updated_catalog = copy.deepcopy(catalog)
                updated_catalog[service_id].pop(index)
                _persist_catalog(updated_catalog)

    st.subheader("Add an image")
    new_image = st.file_uploader(
        "Choose a JPEG, PNG, or WebP image (maximum 10 MB)",
        type=["jpg", "jpeg", "png", "webp"],
        max_upload_size=10,
        key=f"catalog-add-{service_id}",
    )
    new_title = st.text_input("New image title", key=f"catalog-new-title-{service_id}", max_chars=120)
    new_description = st.text_area(
        "New image description",
        key=f"catalog-new-description-{service_id}",
        max_chars=500,
    )
    if st.button("Add image to service", key=f"catalog-add-button-{service_id}"):
        if not new_title.strip():
            st.error("Enter a title for the new image.")
        elif new_image is None:
            st.error("Choose an image file first.")
        else:
            try:
                uploaded = upload_catalog_image(service_id, new_image)
                updated_catalog = copy.deepcopy(catalog)
                updated_catalog[service_id].append(
                    {
                        **uploaded,
                        "icon": "🖼️",
                        "title": new_title.strip(),
                        "description": new_description.strip(),
                    }
                )
                _persist_catalog(updated_catalog)
            except CatalogStorageError as error:
                st.error(str(error))
