import aiohttp_jinja2
from aiohttp.web import View, json_response

from src.models.user import User
from src.db_settings import objects


class Signup(View):

    @aiohttp_jinja2.template('signup.html')
    async def get(self):
        pass

    async def post(self):
        data = await self.request.json()

        try:
            login = data['login']
            password = data['password']

        except KeyError:
            returned_data = dict(
                status='fail',
                message='Provide all the data!'
            )
            return json_response(returned_data, status=400)

        try:
            existing_user = await objects.get(User, login=login, password=password)
            if existing_user:
                returned_data = dict(
                    status='fail',
                    message='User with this login already exists'
                )
                return json_response(returned_data, status=400)

        except User.DoesNotExist:
            await objects.create(User, login=login, password=password)

        returned_data = dict(
            status='success',
            login=login,
            message='You are successfully registered!',
            redirect_link='/login/',
        )
        return json_response(returned_data, status=200)
