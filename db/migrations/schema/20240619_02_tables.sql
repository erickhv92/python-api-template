-- Create base tables with relationships

-- Enable UUID generation
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table
CREATE TABLE IF NOT EXISTS "users" (
  "id" SERIAL PRIMARY KEY,
  "uuid" UUID NOT NULL DEFAULT uuid_generate_v4(),
  "created_at" TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  "updated_at" TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  "active" BOOLEAN NOT NULL DEFAULT TRUE,
  "email" TEXT NOT NULL UNIQUE,
  "password_hash" TEXT NOT NULL,
  "first_name" TEXT,
  "last_name" TEXT,
  "user_type" user_type_enum NOT NULL,
  "last_login" TIMESTAMPTZ
);

-- Projects table
CREATE TABLE IF NOT EXISTS "projects" (
  "id" SERIAL PRIMARY KEY,
  "uuid" UUID NOT NULL DEFAULT uuid_generate_v4(),
  "created_at" TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  "updated_at" TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  "active" BOOLEAN NOT NULL DEFAULT TRUE,
  "name" TEXT NOT NULL,
  "description" TEXT,
  "owner_id" INT REFERENCES users(id)
);

-- Items table
CREATE TABLE IF NOT EXISTS "items" (
  "id" SERIAL PRIMARY KEY,
  "uuid" UUID NOT NULL DEFAULT uuid_generate_v4(),
  "created_at" TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  "updated_at" TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  "active" BOOLEAN NOT NULL DEFAULT TRUE,
  "project_id" INT NOT NULL REFERENCES projects(id),
  "name" TEXT NOT NULL,
  "description" TEXT,
  "status" status_enum NOT NULL DEFAULT 'pending',
  "metadata" JSONB
);

-- Link table example
CREATE TABLE IF NOT EXISTS "project_members" (
  "project_id" INT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
  "user_id" INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  "created_at" TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  "role" TEXT NOT NULL,
  "permissions" JSONB,
  PRIMARY KEY (project_id, user_id)
);

-- Create updated_at function and triggers
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Add triggers for updated_at
DO $$ 
DECLARE
    t text;
BEGIN
    FOR t IN 
        SELECT table_name FROM information_schema.tables 
        WHERE table_schema = 'public' 
        AND table_name IN ('users', 'projects', 'items')
    LOOP
        EXECUTE format('DROP TRIGGER IF EXISTS update_timestamp ON %I', t);
        EXECUTE format(
            'CREATE TRIGGER update_timestamp BEFORE UPDATE ON %I 
             FOR EACH ROW EXECUTE FUNCTION update_modified_column()', 
            t
        );
    END LOOP;
END $$;