# Currency Converter (Streamlit + Frankfurter API)

Student: Kirthi Ramesh 
Student ID: 25130651

Overview
streamlit web app that fetches **currency codes** and **exchange rates** from the Frankfurter API.

Features:
- Get latest conversion rate for two currencies
- Convert a custom amount
- Get historical rate for a chosen date
- Show inverse conversion rate

Files
- `app.py` — Streamlit UI
- `api.py` — HTTP helper
- `frankfurter.py` — API wrapper functions
- `currency.py` — Formatting functions
- `README.md` — Documentation
- `requirements.txt` — Dependencies

Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```


