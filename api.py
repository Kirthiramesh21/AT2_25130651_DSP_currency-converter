import requests
from typing import Any, Dict, Optional

DEFAULT_TIMEOUT = 12

class ApiError(Exception):
    pass

def get_json(url: str, params: Optional[Dict[str, Any]] = None, timeout: int = DEFAULT_TIMEOUT) -> Dict[str, Any]:
    try:
        resp = requests.get(url, params=params, timeout=timeout)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        raise ApiError(str(e))
