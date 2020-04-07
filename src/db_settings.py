import peewee_async
from src.db_data import database
from src.models.base import BaseModel
from src.models.user import User
from src.models.message import Message


database.connect()
database.create_tables([BaseModel, User, Message])
database.close()
objects = peewee_async.Manager(database)
