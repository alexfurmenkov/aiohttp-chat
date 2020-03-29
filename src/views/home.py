from aiohttp import web


async def home(request):
    if request.user is None:
        returned_data = dict(
            status=200,
            message='Hello from Server! You are not logged in!'
        )
    else:
        returned_data = dict(
            status=200,
            message='Hello from Server! You are logged in!'
        )
    return web.json_response(returned_data)
