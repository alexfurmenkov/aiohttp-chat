from aiohttp import web
import aiohttp_jinja2

from src.decorators.login_required import login_required

from src.models.message import Message
from src.db_settings import objects


class Chat(web.View):
    @login_required
    @aiohttp_jinja2.template('chat.html')
    async def get(self):
        return dict(
            status='online',
            button_text='Logout',
            messages=await objects.execute(Message.select()),
        )
