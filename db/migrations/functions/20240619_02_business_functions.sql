-- Business-specific functions

-- Function to handle business-specific logic
CREATE OR REPLACE FUNCTION calculate_project_stats(project_id INTEGER)
RETURNS TABLE (
    total_items INTEGER,
    pending_items INTEGER,
    completed_items INTEGER,
    cancelled_items INTEGER,
    failed_items INTEGER,
    completion_rate NUMERIC
) AS $$
DECLARE
    total INTEGER;
    pending INTEGER;
    completed INTEGER;
    cancelled INTEGER;
    failed INTEGER;
    completion NUMERIC;
BEGIN
    -- Get total items
    SELECT COUNT(*) INTO total
    FROM items
    WHERE project_id = calculate_project_stats.project_id
    AND active = TRUE;
    
    -- Get pending items
    SELECT COUNT(*) INTO pending
    FROM items
    WHERE project_id = calculate_project_stats.project_id
    AND status = 'pending'
    AND active = TRUE;
    
    -- Get completed items
    SELECT COUNT(*) INTO completed
    FROM items
    WHERE project_id = calculate_project_stats.project_id
    AND status = 'completed'
    AND active = TRUE;
    
    -- Get cancelled items
    SELECT COUNT(*) INTO cancelled
    FROM items
    WHERE project_id = calculate_project_stats.project_id
    AND status = 'cancelled'
    AND active = TRUE;
    
    -- Get failed items
    SELECT COUNT(*) INTO failed
    FROM items
    WHERE project_id = calculate_project_stats.project_id
    AND status = 'failed'
    AND active = TRUE;
    
    -- Calculate completion rate
    IF total > 0 THEN
        completion := (completed::NUMERIC / total) * 100;
    ELSE
        completion := 0;
    END IF;
    
    -- Return values
    total_items := total;
    pending_items := pending;
    completed_items := completed;
    cancelled_items := cancelled;
    failed_items := failed;
    completion_rate := completion;
    
    RETURN NEXT;
END;
$$ LANGUAGE plpgsql;