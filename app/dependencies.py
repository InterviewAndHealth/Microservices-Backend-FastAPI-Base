from typing import Annotated
from fastapi import Header, HTTPException


# Autorization header
async def authorize(authorization: Annotated[str, Header()] = None):
    """Authorize requests."""
    pass
