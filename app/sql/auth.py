from sqlalchemy import text
INSERT_USER = text("""
    INSERT INTO user(username,hashed_password) values(:username,:hashed_password);
""")

SELECT_USER_BY_USERNAME = text(
    """
    SELECT * FROM user WHERE username=:username;
"""
)