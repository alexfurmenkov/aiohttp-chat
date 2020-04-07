import peewee
from .base import BaseModel
from .user import User


class Message(BaseModel):

    author = peewee.ForeignKeyField(User)
    message = peewee.TextField()
