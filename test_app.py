from pathlib import Path

from streamlit.testing.v1 import AppTest


def test_sample_assertion():
    assert 1 + 1 == 2


def test_pc_assembly_catalog_uses_github_image_urls():
    app = AppTest.from_file(str(Path(__file__).with_name("app.py"))).run()
    markup = "\n".join(element.value for element in app.markdown)

    assert not app.exception
    for filename in ("pca (1).jpeg", "pca (2).jpeg", "pca (3).jpeg"):
        encoded_filename = filename.replace(" ", "%20").replace("(", "%28").replace(")", "%29")
        assert (
            "https://raw.githubusercontent.com/lokeshkumarpuvvada/"
            f"cloudprintagent/main/{encoded_filename}"
        ) in markup
    assert markup.count('data-gallery-step="-1" aria-label="Previous catalog image"') == 3
    assert markup.count('data-gallery-step="1" aria-label="Next catalog image"') == 3


def test_single_image_catalog_has_zoom_close_without_navigation():
    app = AppTest.from_file(str(Path(__file__).with_name("app.py"))).run()
    markup = "\n".join(element.value for element in app.markdown)
    start = markup.index('<section class="detail-group" id="office-lan-details"')
    end = markup.index('<section class="detail-group" id="network-amc-details"', start)
    office_lan_markup = markup[start:end]

    assert 'aria-label="Close enlarged image preview"' in office_lan_markup
    assert 'class="modal-image-nav' not in office_lan_markup
