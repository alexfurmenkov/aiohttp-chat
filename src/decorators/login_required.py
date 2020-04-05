from aiohttp import web


def login_required(function):
    async def wrapper(self, *args, **kwargs):
        if self.request.user is None:
            raise web.HTTPFound('/login/')
        return await function(self, *args, **kwargs)
    return wrapper
