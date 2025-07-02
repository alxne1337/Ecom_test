from fastapi import FastAPI
from img_check.controller import router as nsfw_router

app = FastAPI()

def register_routes(app: FastAPI):
    app.include_router(nsfw_router)

register_routes(app)