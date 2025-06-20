import os
from typing import Any, Dict, List, Optional, Tuple, TypeVar, Union

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar('T')


async def execute_query(
    session: AsyncSession,
    query_path: str,
    params: Optional[Dict[str, Any]] = None,
) -> List[Dict[str, Any]]:
    """Execute a SQL query from a file and return the results as a list of dictionaries."""
    # Read query from file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    query_file = os.path.join(base_dir, "queries", query_path)
    
    with open(query_file, "r") as f:
        query_text = f.read()
    
    # Execute query
    result = await session.execute(text(query_text), params or {})
    
    # Convert to list of dictionaries
    columns = result.keys()
    rows = [dict(zip(columns, row)) for row in result.fetchall()]
    
    return rows


async def execute_query_one(
    session: AsyncSession,
    query_path: str,
    params: Optional[Dict[str, Any]] = None,
) -> Optional[Dict[str, Any]]:
    """Execute a SQL query from a file and return the first result as a dictionary."""
    rows = await execute_query(session, query_path, params)
    return rows[0] if rows else None