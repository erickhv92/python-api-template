from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field


class ResponseBase(BaseModel):
    """Base model for API responses."""
    success: bool = True
    message: Optional[str] = None


class ErrorResponse(ResponseBase):
    """Error response model."""
    success: bool = False
    error_code: Optional[str] = None
    details: Optional[Dict[str, Any]] = None


class PaginatedResponse(ResponseBase):
    """Paginated response model."""
    total: int
    page: int
    page_size: int
    pages: int
    items: List[Any]


class TimestampMixin(BaseModel):
    """Mixin for models with timestamp fields."""
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None