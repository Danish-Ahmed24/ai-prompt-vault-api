# AI Prompt Vault 🚀

A RESTful API for sharing and managing AI prompts with social features built with FastAPI.

## 🎯 Features

### ✅ Implemented
- **Authentication**: JWT-based user registration and login with password hashing
- **Prompts Management**: Full CRUD operations with public/private visibility control
- **Comments System**: Nested comments with pagination and user ownership
- **Authorization**: Resource ownership validation and access control
- **Pagination**: Efficient data loading with page-based navigation

### 🚧 Planned Features
- Reactions system (likes/dislikes) - Database schema ready
- Bookmarking functionality - Database schema ready
- User profile management

## 🛠️ Tech Stack

**Backend Framework:**
- FastAPI (Python 3.11+)
- Uvicorn ASGI server

**Database:**
- MySQL 8.0+
- SQLAlchemy Core (raw SQL with parameterized queries)

**Security:**
- JWT (JSON Web Tokens) for authentication
- pwdlib for password hashing (Argon2)
- SQL injection prevention via parameterized queries

**Validation:**
- Pydantic v2 for request/response validation

## 📁 Project Structure

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

**Architecture Pattern**: 3-layer architecture with clear separation of concerns
- **Router Layer**: HTTP request handling
- **Service Layer**: Business logic and authorization
- **Repository Layer**: Database operations

## 🚀 Getting Started

### Prerequisites
- Python 3.11 or higher
- MySQL 8.0 or higher
- pip for package management

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd AI_PROMPT_VAULT
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup Database**
```bash
# Create database and tables
mysql -u root -p < ddl.sql
```

5. **Configure Environment Variables**

Create `.env` file in root directory:
```env
SECRET_KEY=your-secret-key-here-change-in-production
ALGORITHM=HS256
DB_USER=root
DB_PASSWORD=your-mysql-password
```

6. **Run the application**
```bash
uvicorn app.main:app --reload
```

7. **Access API Documentation**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📊 Database Schema

### Core Tables

**users**
- User accounts with hashed passwords
- Username uniqueness constraint

**prompts**
- User-generated AI prompts
- Public/private visibility control
- Foreign key to users

**comments**
- Nested comments on prompts
- User ownership tracking
- Cascade delete on prompt/user deletion

**reactions** (Ready for implementation)
- Polymorphic design (works for prompts AND comments)
- Like/dislike tracking
- Composite primary key (user_id, target_type, target_id)

**bookmarks** (Ready for implementation)
- User bookmarking system
- Composite primary key (user_id, prompt_id)

## 🔒 Security Features

- ✅ Password hashing with Argon2 (industry standard)
- ✅ JWT token-based authentication with expiration
- ✅ SQL injection prevention (parameterized queries)
- ✅ Resource ownership validation before delete/update
- ✅ Private/public content access control
- ✅ Input validation with Pydantic (length limits, required fields)
- ✅ CORS configuration for controlled access

## 📚 API Endpoints

### Authentication
- `POST /register` - Create new user account
- `POST /token` - Login and get JWT token

### Prompts
- `GET /prompts` - List all public prompts (paginated)
- `GET /prompts/{id}` - Get single prompt details
- `POST /prompts` - Create new prompt (auth required)
- `PUT /prompts/{id}` - Update prompt (auth + ownership required)
- `DELETE /prompts/{id}` - Delete prompt (auth + ownership required)
- `GET /users/me/prompts` - Get current user's prompts (auth required)

### Comments
- `GET /prompts/{id}/comments` - Get comments for a prompt (paginated)
- `POST /prompts/{id}/comments` - Add comment (auth required)
- `DELETE /comments/{id}` - Delete comment (auth + ownership required)

📖 **Full API documentation**: See [docs/API.md](docs/API.md) or visit `/docs` endpoint

## 🧪 Testing

### Manual Testing
1. Start the server: `uvicorn app.main:app --reload`
2. Open Swagger UI: http://localhost:8000/docs
3. Test flow:
   - Register a user → POST /register
   - Login → POST /token (copy the access_token)
   - Click "Authorize" button, paste token
   - Create a prompt → POST /prompts
   - Add a comment → POST /prompts/{id}/comments
   - List prompts → GET /prompts

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ RESTful API design principles
- ✅ JWT authentication & authorization flows
- ✅ Layered architecture pattern (separation of concerns)
- ✅ Complex SQL queries (JOINs, subqueries, aggregations)
- ✅ Input validation and error handling
- ✅ Database transaction management with SQLAlchemy
- ✅ API documentation with OpenAPI/Swagger
- ✅ Security best practices (password hashing, parameterized queries)

## 🔧 Future Improvements

- [ ] Complete reactions system implementation (likes/dislikes)
- [ ] Complete bookmarks functionality
- [ ] Add user profile management endpoints
- [ ] Unit and integration tests (pytest)
- [ ] Rate limiting for API endpoints
- [ ] Logging system (structured logs)
- [ ] Database migrations (Alembic)
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] Deploy to cloud platform

## 📝 License

This is a learning project for educational purposes.

## 👤 Author

Learning FastAPI and Backend Development

---

**Note**: This project focuses on code quality and clean architecture over feature completeness, demonstrating solid fundamentals in backend development.
