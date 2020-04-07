from aiohttp import web


def login_required(function):
    """
    Returns user to the login page if he is not logged in.
    :param function: view
    :return: wrapper
    """
    async def wrapper(self, *args, **kwargs):
        if self.request.user is None:
            raise web.HTTPFound('/login/')
        return await function(self, *args, **kwargs)
    return wrapper
