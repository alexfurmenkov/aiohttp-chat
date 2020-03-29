from src.views.home import home
from src.views.signup import Signup
from src.views.login import Login
from src.middlewares.get_user import get_user

routes = [
    ('GET', '/', home),
    ('GET', '/user/', get_user),
    ('POST', '/signup/', Signup),
    ('POST', '/login/', Login),
]
