from fastapi import APIRouter

from app.services.user import UserService
from app.types.user import UserCreate, User

router = APIRouter(prefix="/users", tags=["users"])

user_service = UserService()


@router.post("/")
async def create_user(user: UserCreate) -> User:
    return await user_service.create_user(user)


@router.get("/{user_id}")
async def get_user(user_id: int):
    return await user_service.get_user(user_id)
