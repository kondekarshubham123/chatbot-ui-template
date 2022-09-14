from fastapi import APIRouter

bot_router = APIRouter(prefix="/chatbot",tags=["Chatbot Backend"])
check_router = APIRouter(prefix="/chatbot",tags=["Check"])