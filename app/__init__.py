import os
from dotenv import load_dotenv

load_dotenv(override=True)


HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", 8000))
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/db")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")
EXCHANGE_NAME = os.getenv("EXCHANGE_NAME", "EXCHANGE_NAME")
SERVICE_NAME = os.getenv("SERVICE_NAME", "SERVICE_NAME")
SERVICE_QUEUE = os.getenv("SERVICE_QUEUE", "SERVICE_QUEUE")
RPC_QUEUE = os.getenv("RPC_QUEUE", "RPC_QUEUE")

TEST_QUEUE = os.getenv("TEST_QUEUE", "TEST_QUEUE")
TEST_RPC = os.getenv("TEST_RPC", "TEST_RPC")

_important_vars = {
    "HOST": HOST,
    "PORT": PORT,
    "DATABASE_URL": DATABASE_URL,
    "REDIS_URL": REDIS_URL,
    "EXCHANGE_NAME": EXCHANGE_NAME,
    "RABBITMQ_URL": RABBITMQ_URL,
    "SERVICE_NAME": SERVICE_NAME,
    "SERVICE_QUEUE": SERVICE_QUEUE,
    "RPC_QUEUE": RPC_QUEUE,
}

for k, v in _important_vars.items():
    if not v:
        raise Exception(f"Missing environment variable: {k}")
