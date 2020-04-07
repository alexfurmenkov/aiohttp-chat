import jwt
from aiohttp.web_response import json_response

from src.models.user import User
from src.views.login import Login
from src.db_settings import objects


async def auth_middleware(app, handler):
    """
    Middleware to check if user is logged in or not
    :param app:
    :param handler: Request handler
    :return: Request handler
    """
    async def middleware(request):
        request.user = None
        jwt_token = request.cookies.get('Authorization', None)
        if jwt_token:
            try:
                payload = jwt.decode(jwt_token, Login.JWT_SECRET, algorithm=Login.JWT_ALGORITHM)
            except (jwt.DecodeError, jwt.ExpiredSignatureError):
                returned_data = dict(
                    status=400,
                    message='Token is invalid',
                )
                return json_response(returned_data)

            user_id = payload['user_id']
            request.user = await objects.get(User, id=user_id)
        return await handler(request)
    return middleware
