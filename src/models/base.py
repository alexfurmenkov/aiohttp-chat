import peewee
from src.db_data import database


class BaseModel(peewee.Model):

    class Meta:
        database = database
