# AI Prompt Vault API

A RESTful API for sharing and managing AI prompts with social features built with FastAPI.

🌐 **Live API**: https://ai-prompt-vault-api-production-0633.up.railway.app/docs

## Features

### Implemented
- **Authentication**: JWT-based user registration and login with password hashing
- **Prompts Management**: Full CRUD operations with public/private visibility control
- **Comments System**: Nested comments with pagination and user ownership
- **Reactions System**: Polymorphic like/dislike system for prompts and comments
- **Authorization**: Resource ownership validation and access control
- **Pagination**: Efficient data loading with page-based navigation

### Future Enhancements
- Bookmarking functionality
- User profile management

## Tech Stack

- FastAPI (Python 3.13)
- MySQL 8.0+ with SQLAlchemy
- JWT authentication with Argon2 password hashing
- Pydantic v2 for validation
- Deployed on Railway

## Quick Start

### Try the Live API
Visit the live API documentation: https://ai-prompt-vault-api-production-0633.up.railway.app/docs

### Test Flow (Live API)
1. **Register a user** (POST /register)
2. **Login** (POST /token) and copy the token
3. **Click "Authorize"** and paste the token
4. **Create a prompt** (POST /prompts)
5. **Add a comment** (POST /prompts/{id}/comments)
6. **Add a reaction** (POST /reactions)
7. **Get reaction stats** (GET /reactions)

## Features

### Implemented
- **Authentication**: JWT-based user registration and login with password hashing
- **Prompts Management**: Full CRUD operations with public/private visibility control
- **Comments System**: Nested comments with pagination and user ownership
- **Reactions System**: Polymorphic like/dislike system for prompts and comments
- **Authorization**: Resource ownership validation and access control
- **Pagination**: Efficient data loading with page-based navigation

### Future Enhancements
- Bookmarking functionality
- User profile management

## Tech Stack

- FastAPI (Python 3.11+)
- MySQL 8.0+ with SQLAlchemy
- JWT authentication with Argon2 password hashing
- Pydantic v2 for validation

## Project Structure

```
app/
├── routers/          # API endpoints (FastAPI routes)
│   ├── prompts_router.py
│   ├── comments_router.py
│   └── auth.py
├── services/         # Business logic layer
│   ├── prompts_service.py
│   └── comments_service.py
├── repos/            # Data access layer
│   ├── prompts_repo.py
│   └── comments_repo.py
├── sql/              # Raw SQL queries
│   ├── prompts_sql.py
│   ├── comments_sql.py
│   └── auth.py
├── schemas/          # Pydantic models
│   ├── prompts_schema.py
│   ├── comments_schema.py
│   └── users_schema.py
├── database.py       # Database connection
└── main.py           # FastAPI application
```

**Architecture Pattern**: 3-layer architecture (Router → Service → Repository)

## Getting Started (Local Development)

### Prerequisites
- Python 3.13+
- MySQL 8.0+

### Installation

1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/ai-prompt-vault-api.git
cd ai-prompt-vault-api
```

2. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Setup database
```bash
# Create database and tables
mysql -u root -p < ddl.sql
```

5. Configure environment variables

Create `.env` file:
```env
SECRET_KEY=your-secret-key-here-change-in-production
ALGORITHM=HS256
DB_USER=root
DB_PASSWORD=your-mysql-password
```

6. Run the application
```bash
# For development
fastapi dev

# For production
uvicorn app.main:app --reload
```

7. Access API documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Deployment

This API is deployed on Railway with automatic deployments from the main branch.

### Environment Variables (Production)
- `DATABASE_URL`: Automatically provided by Railway MySQL service
- `SECRET_KEY`: Your JWT secret key
- `ALGORITHM`: HS256

The application automatically handles MySQL driver configuration for both local development and Railway production environments.

## Database Schema

- **users**: User accounts with authentication
- **prompts**: AI prompts with public/private visibility
- **comments**: Nested comments on prompts
- **reactions**: Polymorphic like/dislike system for prompts and comments
- **bookmarks**: User bookmarking system (schema ready)

## Security

- Argon2 password hashing
- JWT token authentication with expiration
- Parameterized SQL queries (injection prevention)
- Resource ownership validation
- Input validation with length limits

## API Endpoints

### Authentication
- `POST /register` - Create new user account
- `POST /token` - Login and get JWT token

### Prompts
- `GET /prompts` - List all public prompts (paginated)
- `GET /prompts/{id}` - Get single prompt details
- `POST /prompts` - Create new prompt (requires auth)
- `PUT /prompts/{id}` - Update prompt (requires ownership)
- `DELETE /prompts/{id}` - Delete prompt (requires ownership)
- `GET /users/me/prompts` - Get current user's prompts

### Comments
- `GET /prompts/{id}/comments` - Get comments for a prompt (paginated)
- `POST /prompts/{id}/comments` - Add comment (requires auth)
- `DELETE /comments/{id}` - Delete comment (requires ownership)

### Reactions
- `POST /reactions` - Add or update reaction (requires auth)
- `DELETE /reactions` - Remove reaction (requires auth)
- `GET /reactions` - Get reaction stats (public)

Full documentation available at `/docs` endpoint

## Testing

### Live API Testing
Visit https://ai-prompt-vault-api-production-0633.up.railway.app/docs

### Local Testing
Start the server and open http://localhost:8000/docs

Test flow:
1. Register a user (POST /register)
2. Login (POST /token) and copy the token
3. Click "Authorize" and paste the token
4. Create a prompt (POST /prompts)
5. Add a comment (POST /prompts/{id}/comments)
6. Add a reaction (POST /reactions)
7. Get reaction stats (GET /reactions)

## Learning Outcomes

This project demonstrates:
- RESTful API design
- JWT authentication and authorization
- Layered architecture pattern
- Complex SQL queries (JOINs, subqueries, aggregations)
- Input validation and error handling
- Security best practices

## License

Educational project for learning purposes.

