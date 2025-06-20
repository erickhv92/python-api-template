# Database Migrations with Alembic

This directory contains versioned migration scripts managed by Alembic.

## Setup

1. Initialize Alembic (only once):

```bash
alembic init migrations
```

2. Configure `alembic.ini` and `migrations/env.py` to connect to your database

## Creating a Migration

Create a new migration script:

```bash
alembic revision -m "description_of_changes"
```

Edit the generated script to include your changes, or use autogenerate:

```bash
alembic revision --autogenerate -m "description_of_changes"
```

## Running Migrations

Upgrade to the latest version:

```bash
alembic upgrade head
```

Upgrade to a specific version:

```bash
alembic upgrade +1
```

Downgrade to a previous version:

```bash
alembic downgrade -1
```

## Tips

1. Create separate migrations for schema changes and data migrations
2. Always test migrations on a development environment first
3. Create a backup before applying migrations in production
4. Consider using a transaction for safety

## Manual SQL Scripts

For more complex migrations or specific requirements, you can create SQL scripts in the parent directories:

- `../schema/` - For schema changes
- `../functions/` - For database functions and triggers

These scripts can be executed manually or incorporated into Alembic migrations using the `op.execute()` function.