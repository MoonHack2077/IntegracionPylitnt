"""
This module contains the API key authentication for the application.

Contains the following:

- api_key_header: API key header
- get_api_key: Get the API key

"""

import os
from fastapi import HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "x-api-key"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(api_key_header: str = Security(api_key_header)):
    """
    Get the API key.

    Args:
    - api_key_header (str): The API key from the x-api-key header.

    Raises:
    - HTTPException: If the API key is invalid.

    Returns:
    - str: The API key.

    """
    if api_key_header == API_KEY:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail={
            "status": "false",
            "message": "Unauthorized",
            "status_code": status.HTTP_403_FORBIDDEN,
        },
    )
