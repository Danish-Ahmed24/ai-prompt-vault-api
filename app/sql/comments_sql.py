from sqlalchemy import text

GET_ALL_COMMENTS_GUEST=text(
    """
    SELECT c.id,u.username, c.message, c.created_at
FROM comments c
JOIN users u ON u.id = c.user_id
WHERE c.prompt_id = :prompt_id
ORDER BY c.created_at DESC
LIMIT :limit OFFSET :offset;
"""
)

GET_ALL_COMMENTS_LOGGED = text("""
SELECT 
    c.id,
    CASE 
        WHEN c.user_id = :user_id THEN 'me'
        ELSE u.username
    END AS username,
    c.message,
    c.created_at
FROM comments c
JOIN users u ON u.id = c.user_id
WHERE c.prompt_id = :prompt_id
ORDER BY c.created_at DESC
LIMIT :limit OFFSET :offset;
""")

COUNT_NO_OF_COMMENTS = text(
    """
    SELECT COUNT(*) FROM comments WHERE prompt_id=:prompt_id;
"""
)

ADD_COMMENT=text(
    """
    INSERT INTO comments(user_id,prompt_id,message) VALUES(:user_id,:prompt_id,:message);
"""
)

DELETE_COMMENT = text("""
DELETE FROM comments 
WHERE id = :comment_id 
AND user_id = :user_id;
""")


GET_COMMENT_BY_ID=text(
    """
    SELECT user_id from comments where id=:comment_id;
"""
)