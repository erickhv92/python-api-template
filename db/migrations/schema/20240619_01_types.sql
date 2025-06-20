-- Create custom types/enums

-- Only run if not exists
DO $$ 
BEGIN
    -- User types
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'user_type_enum') THEN
        CREATE TYPE "user_type_enum" AS ENUM (
            'admin',
            'staff', 
            'customer',
            'guest'
        );
    END IF;

    -- Status types
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'status_enum') THEN
        CREATE TYPE "status_enum" AS ENUM (
            'pending',
            'active',
            'completed',
            'cancelled',
            'failed'
        );
    END IF;

    -- Example for additional types
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'priority_enum') THEN
        CREATE TYPE "priority_enum" AS ENUM (
            'low',
            'medium',
            'high',
            'critical'
        );
    END IF;
END $$;