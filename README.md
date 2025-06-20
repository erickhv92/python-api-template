# Python API Template

A template for quickly starting new Python API projects with a standardized structure.

## Project Structure

```
├── application/       # Core application setup and configuration
├── db/                # Database operations and SQL queries
│   ├── migrations/      # Database migration scripts
│   │   ├── schema/       # Table definitions and types
│   │   ├── functions/    # PostgreSQL functions and triggers
│   │   └── versions/     # Alembic versioned migrations
│   └── queries/        # SQL query files for application use
├── helpers/           # Utility functions organized by domain
├── prompts/           # Text prompts for AI models (if applicable)
├── pydantic_schemas/  # Data validation schemas
├── routes/            # API endpoint definitions
├── services/          # External service integrations
├── utils/             # Common utility functions
├── tests/             # Test files
├── docs/              # Documentation
├── main.py            # Application entry point
├── requirements.txt   # Dependencies
└── Dockerfile         # Container definition
```

## Getting Started

1. Clone this template
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment variables
4. Run the application: `python main.py`

## Database Management

This template includes a structured approach to database management:

- `db/migrations/schema/` - SQL scripts for table definitions
- `db/migrations/functions/` - SQL scripts for database functions
- `db/migrations/versions/` - Alembic migration scripts
- `db/queries/` - SQL query files used by the application

### Setting up the database

1. Configure your database connection in `.env`
2. Run initial schema scripts: `python -m scripts.db.setup`
3. Or use Alembic to manage migrations: `alembic upgrade head`

## Development Guidelines

- Use async/await for database operations and external service calls
- Follow the repository pattern for database access
- Validate all input data with Pydantic models
- Document all public functions and endpoints
- Write tests for all business logic

## Deployment

The application is designed to be deployed as a Docker container.

```bash
docker build -t your-app-name .
docker run -p 8000:8000 your-app-name
```