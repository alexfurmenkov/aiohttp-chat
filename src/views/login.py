from aiohttp.web import View, json_response
import jwt
from datetime import datetime, timedelta
from src.db_settings import objects
from src.models.user import User


class Login(View):
    JWT_SECRET = 'secret'
    JWT_ALGORITHM = 'HS256'
    JWT_EXP_TIME = 100

    async def post(self):
        data = await self.request.post()

        if 'login' in data and 'password' in data:
            login = data['login']
            password = data['password']

            try:
                existing_user = await objects.get(User, login=login, password=password)
            except User.DoesNotExist:
                returned_data = dict(
                    status=400,
                    message='User does not exist.'
                )
                return json_response(returned_data)

            payload = dict(
                user_id=existing_user.id,
                exp=datetime.utcnow() + timedelta(hours=self.JWT_EXP_TIME)
            )
            jwt_token = jwt.encode(payload, self.JWT_SECRET, self.JWT_ALGORITHM)

            returned_data = dict(
                status=200,
                message='You are successfully logged in.',
                token=jwt_token.decode('utf-8')
            )
            return json_response(returned_data)
