from typing import Dict, Tuple
from datetime import date as Date
from api import get_json, ApiError

BASE_URL = "https://api.frankfurter.app"

def get_currencies() -> Dict[str, str]:
    return get_json(f"{BASE_URL}/currencies")

def _extract_rate_payload(data: Dict, to_code: str) -> Tuple[float, str]:
    rate = float(data["rates"][to_code])
    dt = data["date"]
    return rate, dt

def get_latest_rate(from_code: str, to_code: str) -> Tuple[float, str]:
    url = f"{BASE_URL}/latest"
    data = get_json(url, params={"from": from_code, "to": to_code})
    return _extract_rate_payload(data, to_code)

def get_historical_rate(on_date: Date, from_code: str, to_code: str) -> Tuple[float, str]:
    url = f"{BASE_URL}/{on_date.strftime('%Y-%m-%d')}"
    data = get_json(url, params={"from": from_code, "to": to_code})
    return _extract_rate_payload(data, to_code)
