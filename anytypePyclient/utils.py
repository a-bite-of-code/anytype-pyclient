import requests
import os
import json
from dotenv import load_dotenv
from typing import Any

load_dotenv()

# Get the config from the environment variable
apiKey = os.getenv("ANYTYPE_API_KEY")
apiUrl = os.getenv("ANYTYPE_BASE_URL")
apiVersion = os.getenv("ANYTYPE_VERSION")

if not apiKey:
    raise RuntimeError("env ANYTYPE_API_KEY not set.")
    
if not apiUrl:
    apiUrl = "http://127.0.0.1:31009/v1"
    
if not apiVersion:
    apiVersion="2025-05-20"
    
class ApiEndPoint:
    def __init__(self) -> None:
        self._baseUrl = apiUrl
        self._headers = {"Authorization": f"Bearer {apiKey}", "Anytype-Version": f"{apiVersion}", "Content-Type": "application/json"}
        
    def requestApi(self, method, url, data={}, params={}) -> Any:
        targetUrl = f"{self._baseUrl}/{url}"
        resp = requests.request(method, targetUrl, data=data, params=params, headers=self._headers)
        resp.raise_for_status()
        return resp
        