from src.views.home import Home
from src.views.signup import Signup
from src.views.login import Login
from src.views.websocket import WebSocket
from src.middlewares.get_user import get_user


url_routes = [
    ('GET', '/', Home),
    ('GET', '/user/', get_user),
    ('*', '/signup/', Signup),
    ('*', '/login/', Login),
    ('GET', '/chat/', WebSocket),
]

static_routes = [
    ('/static/', 'static', 'static'),
    ('/html/', 'static/html', 'html'),
    ('/css/', 'static/css', 'css'),
    ('/fonts/', 'static/fonts', 'fonts'),
    ('/img/', 'static/img', 'img'),
    ('/js/', 'static/js', 'js'),
]
