# Database Migrations

This directory contains SQL migration scripts for database setup and schema changes.

## Structure

- `schema/` - Database schema definitions (tables, types, etc.)
- `functions/` - PostgreSQL functions and triggers
- `versions/` - Versioned migration scripts (if using Alembic)

## Naming Convention

Use the following naming convention for migration files:

```
YYYYMMDD_XX_description.sql
```

Where:
- `YYYYMMDD` is the date (e.g., 20240619)
- `XX` is a sequence number (starting from 01) for multiple migrations on the same day
- `description` is a brief description of what the migration does

Example: `20240619_01_create_initial_tables.sql`

## Guidelines

1. All migrations should be idempotent when possible
2. Include transactions for safety
3. Add comments explaining complex changes
4. Test migrations thoroughly before applying to production

## Migration Management

Migrations can be managed using:

1. Manual execution with tracking
2. Alembic (Python migration tool)
3. Custom migration runner

See `versions/README.md` for more details on using Alembic.