import os
import jinja2
import aiohttp_jinja2
import asyncio
from aiohttp import web
from src.routes import routes
from src.middlewares.auth import auth_middleware


loop = asyncio.get_event_loop()
server = web.Application(loop=loop, middlewares=[auth_middleware])
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')

for route in routes:
    server.router.add_route(route[0], route[1], route[2])

aiohttp_jinja2.setup(server, loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

web.run_app(server, host='localhost', port=8000)
