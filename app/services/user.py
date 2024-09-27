from fastapi import HTTPException

from app import TEST_QUEUE, TEST_RPC
from app.database.repository import UserRepository
from app.database.models import User as UserModel
from app.schemas.user import UserCreate, User as UserSchema
from app.services.broker import EventService, RPCService
from app.types import EVENT_TYPES, RPC_TYPES


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    async def create_user(self, user: UserCreate):
        existing_user = self.repository.get_by_email(user.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        db_user = UserModel(email=user.email, password=user.password)
        saved_user = self.repository.create(db_user)

        await EventService.publish(
            TEST_QUEUE,
            {
                "type": EVENT_TYPES.USER_CREATED,
                "data": {
                    "id": saved_user.id,
                    "email": saved_user.email,
                },
            },
        )

        return UserSchema.model_validate(saved_user)

    async def get_user(self, user_id):
        existing_user = self.repository.get(user_id)
        if not existing_user:
            raise HTTPException(status_code=404, detail="User not found")

        rpc_data = await RPCService.request(
            TEST_RPC,
            {
                "type": RPC_TYPES.TEST_RPC,
                "data": "Requesting data",
            },
        )

        return rpc_data

    @staticmethod
    async def handle_event(event):
        print(f"Received event: {event}")

    @staticmethod
    async def respond_rpc(message):
        print(f"Received RPC: {message}")
        return {"data": "Responding to RPC"}
