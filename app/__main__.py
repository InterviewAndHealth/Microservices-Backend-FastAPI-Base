import uvicorn

from app import HOST, PORT
from app.main import app

uvicorn.run(app, host=HOST, port=PORT)
