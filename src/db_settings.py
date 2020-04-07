import peewee_async
from src.models.base import database
from src.models import *


database.connect()
database.create_tables([BaseModel, User, Message])
database.close()
objects = peewee_async.Manager(database)
