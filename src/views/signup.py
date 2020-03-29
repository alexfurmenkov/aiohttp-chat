from src.models.user import User
from aiohttp.web import View, json_response
from src.db_settings import objects


class Signup(View):

    async def post(self):
        data = await self.request.post()

        if 'login' in data and 'password' in data:
            login = data['login']
            password = data['password']

            try:
                existing_user = await objects.get(User, User.login ** login)
                if existing_user:
                    returned_data = dict(
                        status=400,
                        message='User with this login already exists'
                    )
                    return json_response(returned_data)

            except User.DoesNotExist:
                user = User(login=login, password=password)
                user.save()

            returned_data = dict(
                status=200,
                login=login,
                message='You are successfully registered!'
            )
            return json_response(returned_data)

        else:
            returned_data = dict(
                status=400,
                message='Provide all the data!'
            )

            return json_response(returned_data)
