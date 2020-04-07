import peewee_async
from src.models.base import database
from src.models.user import User
from src.models.message import Message


database.connect()
database.create_tables([User, Message])
database.close()
objects = peewee_async.Manager(database)
