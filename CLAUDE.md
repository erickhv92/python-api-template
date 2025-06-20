# Claude Code Assistant Guide

This document helps Claude Code effectively work with this codebase.

## Project Structure

This is a FastAPI-based Python API template with the following key components:

- `application/` - Core application setup and configuration
- `db/` - Database operations (migrations and queries)
- `routes/` - API endpoints
- `pydantic_schemas/` - Data validation models
- `services/` - External integrations
- `helpers/` - Domain-specific utility functions
- `utils/` - General utilities

## Key Commands

### Development

- **Run the application**: `python main.py` or `uvicorn main:app --reload`
- **Lint code**: `flake8`
- **Type check**: `mypy .`
- **Run tests**: `pytest tests/`

### Database

- **Apply migrations**: `alembic upgrade head`
- **Create migration**: `alembic revision -m "description"`
- **Setup schema directly**: `python -m scripts.db.setup`

## Common File Locations

- **API routes**: `routes/`
- **Database queries**: `db/queries/`
- **Schema definitions**: `db/migrations/schema/`
- **Data models**: `pydantic_schemas/`

## Project Conventions

- Use async/await for all I/O operations
- SQL queries are stored in separate files in `db/queries/`
- Routes use dependency injection for database access
- Responses use Pydantic models for validation and serialization
- Follow PEP 8 style guidelines
- Document all public functions, classes, and methods

## Adding Features

When adding new features:

1. Start by defining Pydantic schemas for the feature
2. Add SQL queries if needed
3. Implement route handlers
4. Register routes in `routes/__init__.py`
5. Add tests in `tests/`

## Database Operations

Database operations should:

- Use parameterized queries to prevent SQL injection
- Be wrapped in transactions when appropriate
- Use async SQLAlchemy for database access
- Store SQL in separate files when complex

## Troubleshooting

If you encounter issues:

- Check application logs for errors
- Verify database connection
- Ensure environment variables are set correctly
- Check API documentation at `/docs` endpoint