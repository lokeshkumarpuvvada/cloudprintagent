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
