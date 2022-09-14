from fastapi import FastAPI, status, Request
from fastapi.middleware.cors import CORSMiddleware
from werkzeug.middleware.proxy_fix import ProxyFix
from app.main.config import Config
from app.main.chatbot.talk.resource import talk_resource
from app.main.chatbot.check.resource import check_resource

fast_app = FastAPI(
    title="Chatbot Backend",
    description= "FastAPI Setup",
    version=Config.get_application_version()
)

fast_app.wsgi_app = ProxyFix(fast_app.wsgi_app)

origins = ["*"]

fast_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fast_app.include_router(
    talk_resource.bot_router,prefix="/api"
)

fast_app.include_router(
    check_resource.check_router,prefix="/api"
)
