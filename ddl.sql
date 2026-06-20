CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    hashed_password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE prompts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    user_id INT NOT NULL,
    is_private BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE reactions (
    user_id INT NOT NULL,
    target_type ENUM('prompt', 'comment') NOT NULL,
    target_id INT NOT NULL,
    type ENUM('like', 'dislike') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (user_id, target_type, target_id),

    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    prompt_id INT NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (prompt_id) REFERENCES prompts(id) ON DELETE CASCADE
);

CREATE TABLE bookmarks (
    user_id INT NOT NULL,
    prompt_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (user_id, prompt_id),

    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (prompt_id) REFERENCES prompts(id) ON DELETE CASCADE
);
drop table user;
use promptdb;
select * from user;
show tables;

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








INSERT INTO users (username, hashed_password) VALUES
('ali', 'hashed_pass_1'),
('sara', 'hashed_pass_2'),
('usman', 'hashed_pass_3'),
('ayesha', 'hashed_pass_4'),
('bilal', 'hashed_pass_5'),
('hamza', 'hashed_pass_6'),
('zain', 'hashed_pass_7'),
('noor', 'hashed_pass_8'),
('fatima', 'hashed_pass_9'),
('kashif', 'hashed_pass_10');



INSERT INTO prompts (title, content, user_id, is_private) VALUES
('FastAPI Guide', 'Learn FastAPI step by step with examples', 1, FALSE),
('SQL Basics', 'SELECT, INSERT, UPDATE explained simply', 2, FALSE),
('Docker Intro', 'Containerization basics for beginners', 3, FALSE),
('React Hooks', 'useState and useEffect explained', 4, FALSE),
('Node API Design', 'Best practices for REST APIs', 5, FALSE),
('Auth System', 'JWT authentication explained', 1, FALSE),
('Clean Code', 'How to write maintainable code', 6, FALSE),
('System Design Basics', 'Scalability concepts explained', 7, FALSE),
('Python Tips', 'Advanced Python tricks', 8, FALSE),
('DevOps Flow', 'CI/CD pipeline basics', 9, FALSE),
('Private Prompt', 'This is private content', 10, TRUE);


INSERT INTO reactions (user_id, target_type, target_id, type) VALUES
(2, 'prompt', 1, 'like'),
(3, 'prompt', 1, 'like'),
(4, 'prompt', 1, 'like'),
(5, 'prompt', 2, 'like'),
(6, 'prompt', 2, 'dislike'),
(7, 'prompt', 3, 'like'),
(8, 'prompt', 3, 'like'),
(9, 'prompt', 4, 'like'),
(10, 'prompt', 5, 'like'),
(1, 'prompt', 6, 'like'),
(2, 'prompt', 6, 'like'),
(3, 'prompt', 7, 'like'),
(4, 'prompt', 7, 'like'),
(5, 'prompt', 8, 'dislike'),
(6, 'prompt', 9, 'like'),
(7, 'prompt', 10, 'like');

INSERT INTO comments (user_id, prompt_id, message) VALUES
(2, 1, 'Very helpful guide!'),
(3, 1, 'Nice explanation bro'),
(4, 1, 'Can you add auth example?'),

(5, 2, 'SQL is confusing but this helped'),
(6, 2, 'Good for beginners'),

(7, 3, 'Docker still hard for me'),
(8, 3, 'Nice intro'),

(9, 4, 'React hooks finally understood'),
(10, 5, 'REST best practices are important'),

(1, 6, 'JWT section is missing refresh tokens'),
(2, 6, 'Please add OAuth too'),

(3, 7, 'Clean code is underrated'),
(4, 7, 'Agree 100%'),

(5, 8, 'System design needs more diagrams');


INSERT INTO bookmarks (user_id, prompt_id) VALUES
(2, 1),
(3, 1),
(4, 2),
(5, 2),
(6, 3),
(7, 3),
(8, 4),
(9, 5),
(10, 6),
(1, 7),
(2, 7),
(3, 8),
(4, 9),
(5, 10);