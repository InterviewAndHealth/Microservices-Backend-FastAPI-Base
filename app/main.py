import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import SERVICE_QUEUE
from app.routes.users import router as users_router
from app.services.broker import EventService, RPCService
from app.services.user import UserService


@asynccontextmanager
async def lifespan(app: FastAPI):
    tasks = [
        EventService.subscribe(SERVICE_QUEUE, UserService),
        RPCService.respond(UserService),
    ]
    tasks = [asyncio.create_task(task) for task in tasks]
    yield
    [task.cancel() for task in tasks]


app = FastAPI(lifespan=lifespan)

app.include_router(users_router)


@app.get("/")
async def root():
    return {"message": "Service is running"}
