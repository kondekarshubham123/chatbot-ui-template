from app.main.chatbot import check_router

@check_router.get("/check")
def talk_analyze():
    return {"Working": "Fine"}