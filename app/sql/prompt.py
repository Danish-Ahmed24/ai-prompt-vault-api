from sqlalchemy import text

GET_ALL_PROMPTS = text("""
                        SELECT * FROM prompts WHERE is_private=false;
                    """)


GET_PROMPT_BY_ID=text("""
        SELECT * FROM prompts where id=:prompt_id where is_private=false;
""")


INSERT_PROMPT=text(
        """
    INSERT INTO prompts(title,content,user_id,is_private) values (:title,:content,:user_id,:is_private)
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


GET_MY_PROMPTS = text(
    """
    SELECT * FROM prompts WHERE user_id=:user_id;
"""
)