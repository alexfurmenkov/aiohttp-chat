from aiohttp.web_response import json_response


async def get_user(request):
    returned_data = dict(
        status=200,
        user=str(request.user)
    )
    return json_response(returned_data)
