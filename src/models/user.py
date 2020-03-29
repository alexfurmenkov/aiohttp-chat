import peewee
import peewee_async

database = peewee_async.PostgresqlDatabase('aiochat', user='postgres', password='postgres', host='localhost', port=5432)


class User(peewee.Model):
    """Base model with db Meta"""

    login = peewee.CharField(max_length=120)
    password = peewee.CharField(max_length=120)

    class Meta:
        database = database
