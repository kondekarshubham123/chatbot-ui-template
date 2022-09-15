import os
import uvicorn
import typer
# from werkzeug.middleware.proxy_fix import ProxyFix
from app.main.config import Config,basedir
from app import fast_app

manager = typer.Typer()

# fast_app.wsgi_app = ProxyFix(fast_app.wsgi_app)

@manager.command(name='run')
def run():
    port = Config.get_value('port')
    uvicorn.run("manage:fast_app",host="0.0.0.0",port=os.environ.get("PORT", int(port)),use_colors=True)

if __name__ == "__main__":
    manager()