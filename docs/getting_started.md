# Getting Started

## Prerequisites

- Python 3.10 or higher
- PostgreSQL database (or compatible alternative)
- Docker (optional, for containerization)

## Environment Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd python_api_template
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the following environment variables:

```env
# Application settings
ENVIRONMENT=development

# Database settings
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname
DB_POOL_SIZE=5
DB_MAX_OVERFLOW=10

# API settings
API_KEY=your_api_key_here
```

## Running the Application

1. Start the development server:

```bash
python main.py
```

Or:

```bash
uvicorn main:app --reload
```

2. Access the API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Running Tests

```bash
pytest tests/
```

## Project Structure

The project follows a modular structure with clear separation of concerns:

- `application/`: Core application setup and configuration
- `db/`: Database operations and SQL queries
- `helpers/`: Utility functions organized by domain
- `pydantic_schemas/`: Data validation schemas
- `routes/`: API endpoint definitions
- `services/`: External service integrations
- `utils/`: Common utility functions

## Adding New Features

1. Define schema models in `pydantic_schemas/`
2. Add SQL queries in `db/queries/`
3. Create route handlers in `routes/`
4. Add helper functions in `helpers/`
5. Add external service integrations in `services/`
6. Add tests in `tests/`

## Deployment

### Docker

Build and run the Docker container:

```bash
docker build -t your-app-name .
docker run -p 8000:8000 --env-file .env your-app-name
```