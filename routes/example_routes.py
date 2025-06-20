from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from db.queries import execute_query, execute_query_one
from pydantic_schemas.base_schemas import PaginatedResponse, ResponseBase
from utils.database import get_db_session


router = APIRouter(tags=["examples"])


@router.get("/examples", response_model=PaginatedResponse)
async def get_examples(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    status: Optional[str] = None,
    db: AsyncSession = Depends(get_db_session),
):
    """Get a paginated list of examples."""
    # Example implementation
    try:
        # Get total count
        total = 100  # Replace with actual count query
        
        # Calculate pagination values
        pages = (total + page_size - 1) // page_size
        
        # Get items for current page
        items = await execute_query(
            db,
            "example_query.sql",
            {
                "status": status,
                "limit": page_size,
            },
        )
        
        return {
            "success": True,
            "total": total,
            "page": page,
            "page_size": page_size,
            "pages": pages,
            "items": items,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))