"""
Create
Read
Update
Delete
"""
from users.schemas import CreateUser


def create_user(user_in: CreateUser) -> dict:  # раньше был dict(), но он сейчас depricated. Используем model_dump()
    user = user_in.model_dump()
    return {
        "success": True,
        "user": user,
    }
