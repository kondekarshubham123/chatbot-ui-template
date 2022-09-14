from wsgiref.validate import validator
from pydantic import BaseModel

class TalkDTO(BaseModel):
    talk: str