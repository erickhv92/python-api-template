from fastapi import FastAPI

# Import all route modules
from routes import example_routes


def include_all_routes(app: FastAPI) -> None:
    """Include all route modules in the application."""
    # Add all route modules here
    app.include_router(example_routes.router, prefix="/api/v1")