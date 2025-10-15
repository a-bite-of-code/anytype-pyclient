import requests
import os
import random
from dotenv import load_dotenv
from typing import Any

load_dotenv()

ANYTYPE_VERSION="2025-05-20"
ANYTYPE_BASE_URL="http://127.0.0.1:31009/v1"
# Get the config from the environment variable
apiKey = os.getenv("ANYTYPE_API_KEY")

if not apiKey:
    raise RuntimeError("Environment variable ANYTYPE_API_KEY is not set")

class ApiEndPoint:
    def __init__(self) -> None:
        self._baseUrl = ANYTYPE_BASE_URL
        self._headers = {"Authorization": f"Bearer {apiKey}", "Anytype-Version": f"{ANYTYPE_VERSION}", "Content-Type": "application/json"}
        
    def requestApi(self, method, url, data={}, params={}) -> Any:
        targetUrl = f"{self._baseUrl}/{url}"
        resp = requests.request(method, targetUrl, data=data, params=params, headers=self._headers)
        try:
            resp.raise_for_status()
        except Exception as e:
            errCode=resp.json()["code"]
            errMsg=resp.json()["message"]
            raise RuntimeError(f"ErrCode:{errCode},ErrMessage:{errMsg}")
        
        return resp
        
def get_random_color() -> str:
    default_color=["grey", "yellow", "orange", "red", "pink", "purple", "blue", "ice", "teal", "lime"]
    return random.choice(default_color)
    