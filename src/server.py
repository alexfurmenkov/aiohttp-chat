import asyncio
from aiohttp import web
from src.routes import routes
from src.middlewares.auth import auth_middleware

loop = asyncio.get_event_loop()
server = web.Application(loop=loop, middlewares=[auth_middleware])

for route in routes:
    server.router.add_route(route[0], route[1], route[2])

web.run_app(server, host='localhost', port=8000)
