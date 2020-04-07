import jwt

from datetime import datetime, timedelta

import aiohttp_jinja2
from aiohttp.web import View, json_response

from src.db_settings import objects
from src.models.user import User


class Login(View):
    JWT_SECRET = 'secret'
    JWT_ALGORITHM = 'HS256'
    JWT_EXP_TIME = 100

    @aiohttp_jinja2.template('login.html')
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
        except User.DoesNotExist:
            returned_data = dict(
                status='fail',
                message='User does not exist.'
            )
            return json_response(returned_data, status=400)

        payload = dict(
            user_id=existing_user.id,
            exp=datetime.utcnow() + timedelta(hours=self.JWT_EXP_TIME)
        )
        jwt_token = jwt.encode(payload, self.JWT_SECRET, self.JWT_ALGORITHM)

        returned_data = dict(
            status='success',
            message='You are successfully logged in.',
            token=jwt_token.decode('utf-8'),
            redirect_link='/'
        )
        return json_response(returned_data, status=200)
