# Python API Template Guide

This guide explains how to use this template to quickly start a new Python API project.

## Overview

This template provides a standardized structure for building Python APIs with FastAPI. It follows modern best practices including:

- Async/await for non-blocking operations
- Clean architecture with separation of concerns
- Pydantic for data validation
- SQL queries in separate files
- Structured database migrations
- Comprehensive documentation
- Testing infrastructure

## Quick Start

1. **Copy the template**
   
   ```bash
   cp -r python_api_template my_new_project
   cd my_new_project
   ```

2. **Create a virtual environment**
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   
   ```bash
   cp .env.example .env
   # Edit .env with your specific settings
   ```

5. **Set up the database**
   
   ```bash
   # Option 1: Run SQL scripts directly
   python -m scripts.db.setup
   
   # Option 2: Use Alembic migrations
   alembic upgrade head
   ```

6. **Run the application**
   
   ```bash
   python main.py
   ```

## Database Management

The template includes a structured approach to database management with multiple options:

### SQL Migration Scripts

SQL scripts are organized in the following directories:

- `db/migrations/schema/` - Table definitions and custom types
- `db/migrations/functions/` - PostgreSQL functions and triggers

Run these scripts using:

```bash
python -m scripts.db.setup
```

### Alembic Migrations

For version-controlled migrations, use Alembic:

```bash
# Create a new migration
alembic revision -m "description_of_changes"

# Apply migrations
alembic upgrade head

# Rollback migrations
alembic downgrade -1
```

### Query Files

SQL queries used by the application are stored in the `db/queries/` directory. These are accessed using the `execute_query` functions.

## Adding Features

### Create a new API endpoint

1. Define data models in `pydantic_schemas/`
2. Add SQL queries in `db/queries/`
3. Create route handlers in `routes/`
4. Add the router to `routes/__init__.py`

### Example: Adding a User API

1. Create data models (`pydantic_schemas/user_schemas.py`):
   ```python
   from pydantic import BaseModel, EmailStr, Field
   from typing import Optional
   from pydantic_schemas.base_schemas import TimestampMixin

   class UserBase(BaseModel):
       email: EmailStr
       name: str
       is_active: bool = True

   class UserCreate(UserBase):
       password: str

   class UserResponse(UserBase, TimestampMixin):
       id: int
   ```

2. Add SQL query (`db/queries/get_user_by_email.sql`):
   ```sql
   SELECT *
   FROM users
   WHERE email = :email
   LIMIT 1
   ```

3. Create route handler (`routes/user_routes.py`):
   ```python
   from fastapi import APIRouter, Depends, HTTPException
   from sqlalchemy.ext.asyncio import AsyncSession

   from db.queries import execute_query_one
   from pydantic_schemas.user_schemas import UserCreate, UserResponse
   from utils.database import get_db_session

   router = APIRouter(tags=["users"])

   @router.get("/users/{email}", response_model=UserResponse)
   async def get_user(
       email: str,
       db: AsyncSession = Depends(get_db_session),
   ):
       user = await execute_query_one(
           db,
           "get_user_by_email.sql",
           {"email": email},
       )
       if not user:
           raise HTTPException(status_code=404, detail="User not found")
       return user
   ```

4. Add to `routes/__init__.py`:
   ```python
   from routes import user_routes
   
   def include_all_routes(app: FastAPI) -> None:
       app.include_router(example_routes.router, prefix="/api/v1")
       app.include_router(user_routes.router, prefix="/api/v1")
   ```

### Adding a Database Function

1. Create a new SQL file in `db/migrations/functions/`:
   ```sql
   -- db/migrations/functions/20240620_01_custom_function.sql
   CREATE OR REPLACE FUNCTION calculate_stats(project_id INTEGER)
   RETURNS TABLE (
       total_count INTEGER,
       active_count INTEGER,
       percentage NUMERIC
   ) AS $$
   BEGIN
       RETURN QUERY
       SELECT 
           COUNT(*) as total_count,
           COUNT(*) FILTER (WHERE active = TRUE) as active_count,
           CASE
               WHEN COUNT(*) > 0 THEN 
                   (COUNT(*) FILTER (WHERE active = TRUE)::NUMERIC / COUNT(*)::NUMERIC) * 100
               ELSE 0
           END as percentage
       FROM items
       WHERE project_id = calculate_stats.project_id;
   END;
   $$ LANGUAGE plpgsql;
   ```

2. Apply the function:
   ```bash
   python -m scripts.db.setup --functions
   ```

## AI Integration

To add AI capabilities:

1. Add required dependencies to `requirements.txt`
2. Create AI service client in `services/`
3. Add prompts in `prompts/`
4. Create route handlers for AI features

See `docs/ai_integration.md` for detailed examples.

## Testing

Run tests with:

```bash
pytest tests/
```

Add new tests in the `tests/` directory following the existing examples.

## Deployment

### Docker

```bash
docker build -t my-api .
docker run -p 8000:8000 --env-file .env my-api
```

### Cloud Environments

The template is designed to work well with cloud environments like:

- Google Cloud Run
- AWS Lambda (with FastAPI adapter)
- Azure Container Apps
- Heroku

## Further Reading

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)
- [Docker Documentation](https://docs.docker.com/)