import aiohttp_jinja2
from aiohttp.web import View


class Home(View):
    @aiohttp_jinja2.template('index.html')
    async def get(self):
        if self.request.user is None:
            return dict(
                message='Nice to see you!',
                button_text='Login',
            )
        else:
            return dict(
                message=f'Hello, {self.request.user.login}',
                button_text='Logout',
            )
