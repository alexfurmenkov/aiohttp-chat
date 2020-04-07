import peewee
import peewee_async
from .user import User

database = peewee_async.PostgresqlDatabase('aiochat', user='postgres', password='postgres', host='localhost', port=5432)


class Message(peewee.Model):

    author = peewee.ForeignKeyField(User)
    message = peewee.TextField()

    class Meta:
        database = database
