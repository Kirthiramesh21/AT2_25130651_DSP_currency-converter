# Currency Converter (Streamlit + Frankfurter API)

**Student:** _Your Full Name_  
**Student ID:** _Your Student ID_

## Overview
This is a Streamlit web app that fetches **currency codes** and **exchange rates** from the Frankfurter API.

Features:
- Get latest conversion rate for two currencies
- Convert a custom amount
- Get historical rate for a chosen date
- Show inverse conversion rate

## Files
- `app.py` — Streamlit UI
- `api.py` — HTTP helper
- `frankfurter.py` — API wrapper functions
- `currency.py` — Formatting functions
- `README.md` — Documentation
- `requirements.txt` — Dependencies

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deployment
This repo can be deployed directly on [Streamlit Community Cloud](https://share.streamlit.io).
