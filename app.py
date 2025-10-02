import streamlit as st
from datetime import date, timedelta
import pandas as pd
from frankfurter import get_currencies, get_latest_rate, get_historical_rate
from currency import format_conversion_text

st.set_page_config(page_title="Currency Converter (Frankfurter)", page_icon="", layout="centered")

st.title(" Currency Converter")
st.caption("Data source: https://www.frankfurter.app/")

@st.cache_data(show_spinner=False, ttl=3600)
def _cached_currencies():
    return get_currencies()

codes_map = _cached_currencies()
all_codes = sorted(codes_map.keys())

amount = st.number_input("Amount", min_value=0.0, value=100.0, step=1.0, format="%.2f")
from_code = st.selectbox("From currency", all_codes, index=all_codes.index("AUD") if "AUD" in all_codes else 0)
to_code = st.selectbox("To currency", all_codes, index=all_codes.index("USD") if "USD" in all_codes else 0)

# Latest rate
if st.button("Get latest rate"):
    try:
        rate, dt = get_latest_rate(from_code, to_code)
        text, _, _ = format_conversion_text(dt, from_code, to_code, rate, amount)
        st.success(text)
    except Exception as e:
        st.error(f"Error: {e}")

# Historical rate
hist_date = st.date_input("Pick a past date", value=date(2024, 1, 2), max_value=date.today())
if st.button("Get historical rate"):
    try:
        rate, dt = get_historical_rate(hist_date, from_code, to_code)
        text, _, _ = format_conversion_text(dt, from_code, to_code, rate, amount)
        st.info(text)
    except Exception as e:
        st.error(f"Error: {e}")

#  Rate trend over last 3 years 
st.subheader("Rate Trend Over the Last 3 Years")
if st.button("Show 3-Year Trend"):
    try:
        end_date = date.today()
        start_date = end_date - timedelta(days=3*365)
        dates = pd.date_range(start=start_date, end=end_date, freq='MS')  # Monthly
        rates = []

        for d in dates:
            try:
                rate, _ = get_historical_rate(d.date(), from_code, to_code)
                rates.append(rate)
            except:
                rates.append(None)  

        df = pd.DataFrame({'Date': dates, 'Rate': rates})
        df.set_index('Date', inplace=True)
        st.line_chart(df, use_container_width=True)
    except Exception as e:
        st.error(f"Failed to fetch trend: {e}")
