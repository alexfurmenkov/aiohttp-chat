import peewee_async
from src.models.user import database, User
from src.models.message import Message


database.connect()
database.create_tables([User, Message])
database.close()
objects = peewee_async.Manager(database)
