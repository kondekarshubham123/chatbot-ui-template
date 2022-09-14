from app.main.chatbot.talk.dto.talk_dto import TalkDTO
from app.main.config import Config

class TalkService():

    @staticmethod
    def get_response(query: TalkDTO):
        return {"Message":Config.get_responses(query.talk)}