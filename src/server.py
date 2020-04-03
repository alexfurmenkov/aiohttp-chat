import os
import jinja2
import aiohttp_jinja2
import asyncio
from aiohttp import web
from src.routes import url_routes, static_routes
from src.middlewares.auth import auth_middleware


loop = asyncio.get_event_loop()
server = web.Application(loop=loop, middlewares=[auth_middleware])
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'static', 'html')

for static_route in static_routes:
    server.router.add_static(static_route[0], path=static_route[1], name=static_route[2])
print(static_routes)

for url_route in url_routes:
    server.router.add_route(url_route[0], url_route[1], url_route[2])

aiohttp_jinja2.setup(server, loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

web.run_app(server, host='localhost', port=8000)
