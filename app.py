import streamlit as st
from datetime import date
from frankfurter import get_currencies, get_latest_rate, get_historical_rate
from currency import format_conversion_text

st.set_page_config(page_title="Currency Converter (Frankfurter)", page_icon="💱", layout="centered")

st.title("💱 Currency Converter")
st.caption("Data source: https://www.frankfurter.app/")

@st.cache_data(show_spinner=False, ttl=3600)
def _cached_currencies():
    return get_currencies()

codes_map = _cached_currencies()
all_codes = sorted(codes_map.keys())

amount = st.number_input("Amount", min_value=0.0, value=100.0, step=1.0, format="%.2f")
from_code = st.selectbox("From currency", all_codes, index=all_codes.index("AUD") if "AUD" in all_codes else 0)
to_code = st.selectbox("To currency", all_codes, index=all_codes.index("USD") if "USD" in all_codes else 0)

if st.button("Get latest rate"):
    try:
        rate, dt = get_latest_rate(from_code, to_code)
        text, _, _ = format_conversion_text(dt, from_code, to_code, rate, amount)
        st.success(text)
    except Exception as e:
        st.error(f"Error: {e}")

hist_date = st.date_input("Pick a past date", value=date(2024, 1, 2), max_value=date.today())
if st.button("Get historical rate"):
    try:
        rate, dt = get_historical_rate(hist_date, from_code, to_code)
        text, _, _ = format_conversion_text(dt, from_code, to_code, rate, amount)
        st.info(text)
    except Exception as e:
        st.error(f"Error: {e}")
