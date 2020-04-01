from src.models.user import User
from aiohttp.web import View, json_response
from src.db_settings import objects


class Signup(View):

    async def post(self):
        data = await self.request.post()

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
            existing_user = await objects.get(User, User.login ** login)
            if existing_user:
                returned_data = dict(
                    status='fail',
                    message='User with this login already exists'
                )
                return json_response(returned_data, status=400)

        except User.DoesNotExist:
            user = User(login=login, password=password)
            user.save()

        returned_data = dict(
            status='success',
            login=login,
            message='You are successfully registered!'
        )
        return json_response(returned_data, status=200)
