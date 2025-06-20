from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from application.params import get_settings
from routes import include_all_routes


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = get_settings()
    
    app = FastAPI(
        title=settings.app_name,
        description=settings.app_description,
        version=settings.app_version,
        docs_url=None if settings.environment == "production" else "/docs",
        redoc_url=None if settings.environment == "production" else "/redoc",
    )
    
    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include all routes
    include_all_routes(app)
    
    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}
    
    return app