from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
from routes.task import task
from decouple import config

app = FastAPI()
# templates = Jinja2Templates(directory="../client/dist")

print(config("FRONTEND_URL"))

origins = [
    config("FRONTEND_URL"),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task)

# app.mount('/assets', StaticFiles(directory="../client/dist/assets"), 'static')

# @app.get("/{rest_of_path:path}")
# async def react_app(req: Request, rest_of_path: str):
#     return templates.TemplateResponse('index.html', { 'request': req })
