# 👤 Users

## Get Current User Profile
```http
GET /users/me
```

### Response
```json
{
  "id": 1,
  "username": "ali",
  "created_at": "2026-06-20T10:00:00Z"
}
```

---

## Update Profile
```http
PUT /users/me
```

### Request
```json
{
  "username": "new_name"
}
```

# 💬 Comments

## Get Comments of Prompt
```http
GET /prompts/{id}/comments?page=1
```

### Response
```json
[
  {
    "id": 1,
    "message": "Nice prompt!",
    "user": "ali",
    "created_at": "2026-06-20T10:00:00Z"
  }
]
```

---

## Add Comment
```http
POST /prompts/{id}/comments
```

### Request
```json
{
  "message": "Great prompt!"
}
```

---

## Delete Comment
```http
DELETE /comments/{id}
```

---

# ❤️ Reactions (Unified System)

👉 Used for BOTH prompts & comments

## Add / Update Reaction
```http
POST /reactions
```

### Request
```json
{
  "type": "like",
  "target_type": "prompt",
  "target_id": 1
}
```

### Response
```json
{
  "message": "reaction saved"
}
```

---

## Remove Reaction
```http
DELETE /reactions
```

### Request
```json
{
  "target_type": "prompt",
  "target_id": 1
}
```

---

## Get Reactions
```http
GET /reactions?target_type=prompt&target_id=1
```

### Response
```json
{
  "likes": 10,
  "dislikes": 2
}
```

---

# 🔖 Bookmarks

## Get My Bookmarks
```http
GET /bookmarks
```

---

## Add Bookmark
```http
POST /bookmarks
```

### Request
```json
{
  "prompt_id": 1
}
```

---

## Remove Bookmark
```http
DELETE /bookmarks/{id}
```

---

# 📌 General Rules

### Authentication
- All endpoints (except auth) require JWT token

### Pagination
- `page`
- `limit`

### Standard Response Codes
- 200 OK
- 201 Created
- 400 Bad Request
- 401 Unauthorized
- 404 Not Found
- 500 Server Error

---

# 🧠 Design Principles Used

- RESTful resource-based design
- Unified reaction system (polymorphic)
- Minimal nesting (max 2 levels)
- Scalable structure for React & Flutter clients
- Separation of concerns (auth, prompts, comments, reactions)

---