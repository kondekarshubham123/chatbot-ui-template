from app.main.chatbot import bot_router
from app.main.chatbot.talk.dto.talk_dto import TalkDTO
from app.main.chatbot.talk.service.talk_service import TalkService


@bot_router.post("/talk")
def talk_analyze(query: TalkDTO):
    return TalkService.get_response(query)