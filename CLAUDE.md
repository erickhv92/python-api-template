# Claude Code Assistant Guide

This document helps Claude Code effectively work with this codebase and maintain context between sessions.

## IMPORTANT INSTRUCTIONS FOR CLAUDE AGENTS

**ALWAYS UPDATE THIS FILE DURING AND AFTER EACH SESSION!**

1. **Continuous Updates**: Update this file as you work, not just at the end of a session
2. **Task Status**: Mark tasks as in-progress when you start them, completed when done
3. **Context Recording**: Document any important discoveries or decisions made
4. **Change Logging**: Record all significant changes you make to the codebase
5. **Branch Awareness**: Note which branch you're working on and what's happening on other branches

If you are about to run out of context or end a session:
- Ensure this file reflects all current tasks and their status
- Document any partial progress on incomplete tasks
- Note any important context that would help the next agent continue your work

## Branch Coordination

Current active branches:
- `main`: Primary stable branch (production-ready code)
- Example: `feature/user-auth`: User authentication implementation (in progress)

### Multi-Agent Coordination

If multiple Claude agents are working on this project:
1. Always specify which branch you're working on at the start of your work
2. Before creating a new branch, check this file for existing branches
3. When merging branches, update this file to reflect the merged state
4. Document branch dependencies (e.g., "branch X depends on branch Y")

*Note to Claude: Keep this branch list updated. Add new branches when created, remove branches when deleted or merged.*

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

## Task Tracking

### Current Tasks

- [ ] Example task: Add user authentication system
- [ ] Example task: Implement rate limiting middleware
- [ ] Example task: Create API documentation with examples

*Note to Claude: Update this section continuously as you work. Use these status markers:*
- *[ ] Task not started*
- *[~] Task in progress (add notes on current status)*
- *[x] Task completed (add completion date)*

### Recently Completed

- [x] Initial project setup and repository creation (2024-06-20)
- [x] Added database migration structure (2024-06-20)
- [x] Added development configuration files (2024-06-20)
- [x] Enhanced CLAUDE.md with task tracking and project memory (2024-06-20)

### Backlog

- [ ] Example task: Set up Docker Compose for development
- [ ] Example task: Add health check endpoint with database connectivity test
- [ ] Example task: Implement caching layer

### In-Progress Work Details

*Note to Claude: When a task is complex and in progress, provide details here to help continue the work between sessions.*

Example in-progress task details:
```
Task: Add user authentication system
Branch: feature/user-auth
Status: [~] In progress
Current state:
- JWT token generation is implemented
- Password hashing is implemented
- Need to implement token validation middleware
- Need to add user registration endpoint
```

## Change History

### 2024-06-20

- Created initial template structure
- Added database migration system with schema and functions directories
- Added Alembic integration
- Added Claude Code support files and development configuration
- Enhanced CLAUDE.md with task tracking, change history, and project context

### Future changes will be logged here...

*Note to Claude: When making significant changes, add an entry here with the date and a bullet list of changes made. If changes are part of a specific task, reference the task.*

## Project Context

### User Preferences

- **Coding Style**: Prefer explicit over implicit; use type annotations
- **Naming Convention**: snake_case for variables and functions, PascalCase for classes
- **Documentation**: Docstrings should follow Google style
- **Testing**: Aim for >80% code coverage; use pytest fixtures for setup
- **Error Handling**: Use custom exception classes and provide clear error messages

### Domain Knowledge

- **Purpose**: This template serves as a starting point for building Python API services
- **Primary Use Case**: Backend services with database integration and JSON API endpoints
- **Key Entities**: 
  - Users (authentication and authorization)
  - Projects (top-level organizational structure)
  - Items (resources that belong to projects)

### Architecture Decisions

- **Async First**: All I/O operations should be async for scalability
- **Repository Pattern**: Database access is abstracted through query files
- **Clean Architecture**: Separation of concerns between layers
- **Migration Strategy**: Both SQL scripts for direct application and Alembic for versioning

*Note to Claude: Update this section as you learn more about the project or when architectural decisions are made. Document the reasoning behind decisions, not just the decisions themselves.*

## Session Continuity Notes

*Note to Claude: Use this section to leave notes for your future self or other agents. Include any context that would be helpful for continuing work on the project.*

Example session note:
```
Session: 2024-06-20
Branch: main
Work completed:
- Set up initial project structure
- Added database migration system
- Enhanced CLAUDE.md for better project memory

Important context:
- The database schema is designed to be extendable with custom fields
- The migration system supports both direct SQL and Alembic approaches
- The key entity relationships are: Projects -> Items (one-to-many)

Next steps:
- Implement user authentication system
- Add more comprehensive test coverage
- Create API documentation
```

## Required Checks Before Completion

Before considering a task complete, ensure:

1. All code follows the project conventions
2. Tests are added for new functionality
3. Documentation is updated
4. Type hints are properly applied
5. Code passes linting and type checking
6. **This CLAUDE.md file is updated with task status and changes**

## Resources and References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)
- [Pydantic Documentation](https://docs.pydantic.dev/latest/)