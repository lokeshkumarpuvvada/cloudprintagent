# Hanvika IT Solutions - Streamlit Website

## Run locally

```powershell
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local address displayed by Streamlit, normally `http://localhost:8501`.

## Deploy on Streamlit Community Cloud

1. Push the repository to GitHub.
2. In [Streamlit Community Cloud](https://share.streamlit.io/), create an app using repository `lokeshkumarpuvvada/cloudprintagent`, branch `main`, and entrypoint `app.py`.
3. Use the supported Python version shown in the deployment settings. No app secrets are currently required.
4. Choose an available app subdomain, such as `hanvikaits`, to get a URL under `streamlit.app`.

Community Cloud documents customizable `*.streamlit.app` subdomains, not binding a custom domain such as `hanvikaits.com`. No repository setting can attach that domain; use a Streamlit subdomain or a host that supports custom domains. The latter also requires DNS access. Never commit `.streamlit/secrets.toml`; add any future secrets through the app's Cloud settings.