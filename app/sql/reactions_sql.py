from sqlalchemy import text

# Add or update a reaction
UPSERT_REACTION = text("""
    INSERT INTO reactions (user_id, target_type, target_id, type)
    VALUES (:user_id, :target_type, :target_id, :type)
    ON DUPLICATE KEY UPDATE type = :type
""")

# Remove a reaction
DELETE_REACTION = text("""
    DELETE FROM reactions 
    WHERE user_id = :user_id 
    AND target_type = :target_type 
    AND target_id = :target_id
""")

# Get reaction counts for a specific target
GET_REACTION_STATS = text("""
    SELECT 
        SUM(CASE WHEN type = 'like' THEN 1 ELSE 0 END) as likes,
        SUM(CASE WHEN type = 'dislike' THEN 1 ELSE 0 END) as dislikes
    FROM reactions
    WHERE target_type = :target_type 
    AND target_id = :target_id
""")

# Check if a specific target exists (for validation)
CHECK_PROMPT_EXISTS = text("""
    SELECT id FROM prompts WHERE id = :target_id
""")

CHECK_COMMENT_EXISTS = text("""
    SELECT id FROM comments WHERE id = :target_id
""")
