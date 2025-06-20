-- Example query with parameters
SELECT *
FROM items
WHERE status = :status
ORDER BY created_at DESC
LIMIT :limit