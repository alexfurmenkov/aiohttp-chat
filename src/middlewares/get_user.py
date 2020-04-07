from aiohttp.web_response import json_response


async def get_user(request):
    """
    Middleware to return user who sent a request
    :param request: request to a server
    :return: Info about user in JSON format
    """
    returned_data = dict(
        status=200,
        user=str(request.user)
    )
    return json_response(returned_data)
