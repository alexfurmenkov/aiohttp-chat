from src.views.home import Home
from src.views.signup import Signup
from src.views.login import Login
from src.middlewares.get_user import get_user


url_routes = [
    ('GET', '/', Home),
    ('GET', '/user/', get_user),
    ('POST', '/signup/', Signup),
    ('GET', '/signup.html', Signup),
    ('POST', '/login/', Login),
    ('GET', '/login.html', Login),
]

static_routes = [
    ('/css/', 'static/css', 'css'),
    ('/fonts/', 'static/fonts', 'fonts'),
    ('/img/', 'static/img', 'img'),
    ('/js/', 'static/js', 'js'),
]
