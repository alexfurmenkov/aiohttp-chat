import peewee
import peewee_async

database = peewee_async.PostgresqlDatabase('aiochat',
                                           user='postgres',
                                           password='postgres',
                                           host='localhost',
                                           port=5432)


class BaseModel(peewee.Model):

    class Meta:
        database = database
