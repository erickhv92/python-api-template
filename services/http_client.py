import json
from typing import Any, Dict, Optional, Union

import httpx

from utils.logging import setup_logging


logger = setup_logging(__name__)


class HttpClient:
    """HTTP client for making API requests."""
    
    def __init__(self, base_url: str = "", timeout: float = 10.0):
        self.base_url = base_url
        self.timeout = timeout
        self.default_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
    
    async def request(
        self,
        method: str,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Make an HTTP request."""
        full_url = f"{self.base_url}{url}" if self.base_url and not url.startswith("http") else url
        
        # Merge headers
        merged_headers = {**self.default_headers}
        if headers:
            merged_headers.update(headers)
        
        # Use the specified timeout or the default
        request_timeout = timeout or self.timeout
        
        try:
            async with httpx.AsyncClient(timeout=request_timeout) as client:
                response = await client.request(
                    method,
                    full_url,
                    params=params,
                    json=data,
                    headers=merged_headers,
                )
                
                # Log request details
                logger.debug(
                    f"HTTP request: {method} {full_url}",
                    extra={"props": {"status_code": response.status_code}},
                )
                
                # Raise for status
                response.raise_for_status()
                
                # Parse response
                if response.headers.get("content-type", "").startswith("application/json"):
                    return response.json()
                else:
                    return {"text": response.text}
        except httpx.HTTPStatusError as e:
            logger.error(
                f"HTTP error: {e.response.status_code} - {e.response.text}",
                extra={"props": {"url": full_url, "method": method}},
            )
            raise
        except httpx.RequestError as e:
            logger.error(
                f"Request error: {str(e)}",
                extra={"props": {"url": full_url, "method": method}},
            )
            raise
    
    async def get(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Make a GET request."""
        return await self.request("GET", url, params=params, headers=headers)
    
    async def post(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Make a POST request."""
        return await self.request("POST", url, params=params, data=data, headers=headers)