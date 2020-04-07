import peewee
from .base import BaseModel


class User(BaseModel):

    login = peewee.CharField(max_length=120)
    password = peewee.CharField(max_length=120)

