from sqlalchemy import text

GET_ALL_PROMPTS_FOR_GUEST_USER = text("""
SELECT 
    p.id,
    p.title,
    p.content,
    u.username AS author,
    p.created_at,
    COALESCE(r.likes_count,0) AS likes_count,
    COALESCE(r.dislikes_count,0) AS dislikes_count,
    COALESCE(c.comments_count,0) AS comments_count
FROM prompts p
JOIN users u ON u.id = p.user_id
LEFT JOIN 
	(
		SELECT 
			target_id,
            SUM(type='like') as likes_count,
            SUM(type='dislike') as dislikes_count
		FROM reactions 
        WHERE target_type = 'prompt'
        GROUP BY target_id
    ) r ON r.target_id = p.id
LEFT JOIN (
	SELECT 
		prompt_id,
        COUNT(user_id) as comments_count
        FROM comments
        GROUP BY prompt_id
) c 
    ON c.prompt_id = p.id
WHERE p.is_private = FALSE
ORDER BY p.created_at DESC;

                    """)

GET_ALL_PROMPTS_FOR_LOGGED_USER = text("""
SELECT 
    p.id,
    p.title,
    p.content,
    u.username AS author,
    p.created_at,
    COALESCE(r.likes_count,0) AS likes_count,
    COALESCE(r.dislikes_count,0) AS dislikes_count,
    COALESCE(c.comments_count,0) AS comments_count,
    COALESCE((SELECT DISTINCT 1 FROM bookmarks WHERE user_id=:user_id AND prompt_id=p.id),0) as bookmarked,
    COALESCE((select type from reactions where user_id=:user_id AND target_id=p.id AND target_type='prompt'),'none') as my_reaction
FROM prompts p
JOIN users u ON u.id = p.user_id
LEFT JOIN 
	(
		SELECT 
			target_id,
            SUM(type='like') as likes_count,
            SUM(type='dislike') as dislikes_count
		FROM reactions 
        WHERE target_type = 'prompt'
        GROUP BY target_id
    ) r ON r.target_id = p.id
LEFT JOIN (
	SELECT 
		prompt_id,
        COUNT(user_id) as comments_count
        FROM comments
        GROUP BY prompt_id
) c 
    ON c.prompt_id = p.id
WHERE (p.is_private = FALSE OR p.user_id = :user_id)
ORDER BY p.created_at DESC;

                    """)

GET_PROMPT_BY_ID_GUEST=text("""
        SELECT 
    p.id,
    p.title,
    p.content,
    u.username AS author,
    p.created_at,
    COALESCE(r.likes_count,0) AS likes_count,
    COALESCE(r.dislikes_count,0) AS dislikes_count,
    COALESCE(c.comments_count,0) AS comments_count
FROM prompts p
JOIN users u ON u.id = p.user_id
LEFT JOIN 
	(
		SELECT 
			target_id,
            SUM(type='like') as likes_count,
            SUM(type='dislike') as dislikes_count
		FROM reactions 
        WHERE target_type = 'prompt'
        GROUP BY target_id
    ) r ON r.target_id = p.id
LEFT JOIN (
	SELECT 
		prompt_id,
        COUNT(user_id) as comments_count
        FROM comments
        GROUP BY prompt_id
) c 
    ON c.prompt_id = p.id
WHERE p.is_private = FALSE and p.id=:prompt_id;
""")

GET_PROMPT_BY_ID_LOGGED=text("""
    SELECT 
    p.id,
    p.title,
    p.content,
    u.username AS author,
    p.created_at,
    COALESCE(r.likes_count,0) AS likes_count,
    COALESCE(r.dislikes_count,0) AS dislikes_count,
    COALESCE(c.comments_count,0) AS comments_count,
    COALESCE((SELECT DISTINCT 1 FROM bookmarks WHERE user_id=:user_id AND prompt_id=p.id),0) as bookmarked,
    COALESCE((select type from reactions where user_id=:user_id AND target_id=p.id AND target_type='prompt'),'none') as my_reaction
FROM prompts p
JOIN users u ON u.id = p.user_id
LEFT JOIN 
	(
		SELECT 
			target_id,
            SUM(type='like') as likes_count,
            SUM(type='dislike') as dislikes_count
		FROM reactions 
        WHERE target_type = 'prompt'
        GROUP BY target_id
    ) r ON r.target_id = p.id
LEFT JOIN (
	SELECT 
		prompt_id,
        COUNT(user_id) as comments_count
        FROM comments
        GROUP BY prompt_id
) c 
    ON c.prompt_id = p.id
WHERE p.id = :prompt_id AND (p.is_private = FALSE OR p.user_id = :user_id)
ORDER BY p.created_at DESC;

""")

GET_MY_PROMPTS = text(
    """
SELECT 
    p.id,
    p.title,
    p.content,
    u.username AS author,
    p.created_at,
    COALESCE(r.likes_count,0) AS likes_count,
    COALESCE(r.dislikes_count,0) AS dislikes_count,
    COALESCE(c.comments_count,0) AS comments_count,
    COALESCE((SELECT DISTINCT 1 FROM bookmarks WHERE user_id=:user_id AND prompt_id=p.id),0) as bookmarked,
    COALESCE((select type from reactions where user_id=:user_id AND target_id=p.id AND target_type='prompt'),'none') as my_reaction
FROM prompts p
JOIN users u ON u.id = p.user_id
LEFT JOIN 
	(
		SELECT 
			target_id,
            SUM(type='like') as likes_count,
            SUM(type='dislike') as dislikes_count
		FROM reactions 
        WHERE target_type = 'prompt'
        GROUP BY target_id
    ) r ON r.target_id = p.id
LEFT JOIN (
	SELECT 
		prompt_id,
        COUNT(user_id) as comments_count
        FROM comments
        GROUP BY prompt_id
) c 
    ON c.prompt_id = p.id
WHERE p.user_id=:user_id
ORDER BY p.created_at DESC;

"""
)








INSERT_PROMPT=text(
        """
    INSERT INTO prompts(title,content,user_id,is_private) values (:title,:content,:user_id,:is_private);
"""
    )


DELETE_PROMPT_BY_ID=text(
        """
        DELETE from prompts where id = :prompt_id and user_id=:user_id
"""
    )


UPDATE_PROMPT_BY_ID = text(
        """
    UPDATE prompts set title=:title, content=:content where id=:prompt_id and user_id=:user_id
"""
    )


