-- Utility functions for database operations

-- Function to perform dynamic upsert operations
CREATE OR REPLACE FUNCTION dynamic_upsert(
    table_name TEXT,
    json_data JSONB
) RETURNS JSONB AS $$
DECLARE
    sql_stmt TEXT;
    columns TEXT := '';
    values TEXT := '';
    set_clause TEXT := '';
    column_name TEXT;
    column_value TEXT;
    record_exists BOOLEAN;
    record_id TEXT;
    action_type TEXT;
    result JSONB := '[]'::JSONB; -- Initialize empty JSON array
BEGIN
    -- Extract ID (assuming all records have an "id")
    record_id := json_data->>'id';

    -- Check if the record exists
    EXECUTE format('SELECT EXISTS (SELECT 1 FROM %I WHERE id = %L)', table_name, record_id)
    INTO record_exists;

    IF record_exists THEN
        -- *********** UPDATE LOGIC ***********
        -- Build the SET clause dynamically
        FOR column_name, column_value IN
            SELECT key, value FROM jsonb_each_text(json_data)
            WHERE key <> 'id' -- Exclude ID from update
        LOOP
            set_clause := set_clause || format('%I = %L, ', column_name, column_value);
        END LOOP;

        -- Remove trailing comma
        set_clause := left(set_clause, length(set_clause) - 2);

        -- Construct and execute the UPDATE query dynamically
        sql_stmt := format('UPDATE %I SET %s WHERE id = %L;', table_name, set_clause, record_id);
        EXECUTE sql_stmt;

        -- Set action type
        action_type := 'update';

    ELSE
        -- *********** INSERT LOGIC ***********
        -- Build the column list and values dynamically
        FOR column_name, column_value IN
            SELECT key, value FROM jsonb_each_text(json_data)
        LOOP
            columns := columns || format('%I, ', column_name);
            values := values || format('%L, ', column_value);
        END LOOP;

        -- Remove trailing commas
        columns := left(columns, length(columns) - 2);
        values := left(values, length(values) - 2);

        -- Construct and execute the INSERT query dynamically
        sql_stmt := format('INSERT INTO %I (%s) VALUES (%s) RETURNING id;', table_name, columns, values);
        EXECUTE sql_stmt INTO record_id;

        -- Set action type
        action_type := 'insert';
    END IF;

    -- Append the result to JSON array
    result := result || jsonb_build_object('id', record_id, 'action', action_type);

    RETURN result;
END;
$$ LANGUAGE plpgsql;

-- Function to get enum values
CREATE OR REPLACE FUNCTION get_enum_values(enum_name TEXT)
RETURNS TABLE(value TEXT) AS $$
BEGIN
    RETURN QUERY EXECUTE format(
        'SELECT unnest(enum_range(NULL::%I))::text AS value',
        enum_name
    );
END;
$$ LANGUAGE plpgsql;