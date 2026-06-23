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
