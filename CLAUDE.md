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

## File Management Strategy

To prevent this file from becoming too large:

1. **Active Content Only**: Only keep information that's actively useful
2. **Archive Regularly**: 
   - Move completed tasks older than 2 weeks to archive
   - Archive change history older than 1 month
   - Create archive files when needed (see below)

3. **Focus on Current Context**:
   - Keep detailed notes only for active work
   - Summarize completed work instead of keeping detailed notes

4. **Archiving Process**:
   - When this file exceeds ~500 lines, it's time to archive
   - Create dated archive files in the `docs/archives/` directory
   - Example: `docs/archives/CLAUDE_ARCHIVE_2024_06.md`
   - Move older completed tasks and change history to the archive
   - Keep a summary of key archived decisions and changes

5. **Section Size Limits**:
   - Recently Completed Tasks: Max 10 entries (then archive)
   - Change History: Max 1 month (then archive)
   - In-Progress Work Details: Only current tasks

Remember: This file should be a helpful tool, not a bureaucratic burden. Keep it focused on what's needed for current work.

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

*Note to Claude: When a task is complex and in progress, provide details here to help continue the work between sessions. Remove details once a task is completed.*

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

## Key Decisions & Architecture

*Note to Claude: Keep this section focused and concise. Only include decisions that affect how the code should be written or understood.*

- **Async First**: All I/O operations should be async for scalability
- **Repository Pattern**: Database access is abstracted through query files
- **Clean Architecture**: Separation of concerns between layers
- **Migration Strategy**: Both SQL scripts for direct application and Alembic for versioning

## Current Session Notes

*Note to Claude: Update this section at the beginning and end of each session. Overwrite the previous session notes.*

```
Session: 2024-06-20
Branch: main
Current focus:
- Setting up project template structure
- Adding database migration system
- Improving project documentation

Key context:
- The database schema is designed to be extendable with custom fields
- The migration system supports both direct SQL and Alembic approaches

Next steps:
- Implement user authentication system
- Add more comprehensive test coverage
- Create API documentation
```

## Recent Changes

*Note to Claude: Keep only the last 2-4 weeks of changes here. Older entries should be moved to an archive file.*

### 2024-06-20

- Created initial template structure
- Added database migration system with schema and functions directories
- Added Alembic integration
- Added Claude Code support files and development configuration
- Enhanced CLAUDE.md with task tracking, change history, and project context

## Required Checks Before Completion

Before considering a task complete, ensure:

1. All code follows the project conventions
2. Tests are added for new functionality
3. Documentation is updated
4. Type hints are properly applied
5. Code passes linting and type checking
6. This CLAUDE.md file is updated with task status and changes

## Resources and References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)
- [Pydantic Documentation](https://docs.pydantic.dev/latest/)