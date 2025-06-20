from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Union


def flatten_dict(d: Dict[str, Any], parent_key: str = "", sep: str = "_") -> Dict[str, Any]:
    """Flatten a nested dictionary."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def paginate_list(items: List[Any], page: int, page_size: int) -> Dict[str, Any]:
    """Paginate a list of items."""
    total = len(items)
    pages = (total + page_size - 1) // page_size if total > 0 else 0
    
    # Adjust page number if out of bounds
    if page > pages and pages > 0:
        page = pages
    
    # Calculate slice indices
    start = (page - 1) * page_size
    end = start + page_size
    
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "pages": pages,
        "items": items[start:end] if total > 0 else [],
    }