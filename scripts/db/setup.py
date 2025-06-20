#!/usr/bin/env python

"""Database setup script.

This script runs the SQL migration scripts to set up the database schema.

Usage:
    python -m scripts.db.setup [--schema] [--functions]

Options:
    --schema      Run schema scripts (default: True)
    --functions   Run function scripts (default: True)
"""

import os
import sys
import argparse
import asyncio
from typing import List, Optional

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

from application.params import get_settings


async def run_sql_scripts(directory: str, engine) -> None:
    """Run all SQL scripts in a directory."""
    # Check if directory exists
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return

    # Get all SQL files
    files = sorted([f for f in os.listdir(directory) if f.endswith(".sql")])
    
    if not files:
        print(f"No SQL files found in {directory}")
        return
    
    print(f"Running {len(files)} SQL scripts from {directory}...")
    
    # Execute each file
    async with engine.begin() as conn:
        for file in files:
            file_path = os.path.join(directory, file)
            print(f"  Running {file}...")
            
            with open(file_path, "r") as f:
                sql = f.read()
                await conn.execute(text(sql))
                
            print(f"  ✓ Completed {file}")


async def main(schema: bool = True, functions: bool = True) -> None:
    """Run database setup scripts."""
    settings = get_settings()
    
    # Create engine
    engine = create_async_engine(
        settings.database_url,
        echo=False,
    )
    
    # Get base directory
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    migrations_dir = os.path.join(base_dir, "db", "migrations")
    
    # Run schema scripts
    if schema:
        schema_dir = os.path.join(migrations_dir, "schema")
        await run_sql_scripts(schema_dir, engine)
    
    # Run function scripts
    if functions:
        functions_dir = os.path.join(migrations_dir, "functions")
        await run_sql_scripts(functions_dir, engine)
    
    print("\nDatabase setup complete!")


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description="Set up the database schema and functions.")
    parser.add_argument("--schema", action="store_true", default=True, 
                        help="Run schema scripts (default: True)")
    parser.add_argument("--functions", action="store_true", default=True,
                        help="Run function scripts (default: True)")
    
    args = parser.parse_args()
    
    # Run the main function
    asyncio.run(main(schema=args.schema, functions=args.functions))