from sqlalchemy import text

GET_ALL_PROMPTS = text("""
                        SELECT * FROM prompt;
                    """)


GET_PROMPT_BY_ID=text("""
        SELECT * FROM prompt where id=:prompt_id;
""")


INSERT_PROMPT=text(
        """
    INSERT INTO prompt(title,content) values (:title,:content)
"""
    )


DELETE_PROMPT_BY_ID=text(
        """
        DELETE from prompt where id = :prompt_id
"""
    )


UPDATE_PROMPT_BY_ID = text(
        """
    UPDATE prompt set title=:title, content=:content where id=:prompt_id
"""
    )