import peewee_async
from src.models.user import database, User


database.connect()
database.create_tables([User])
database.close()
objects = peewee_async.Manager(database)
database.set_allow_sync(False)
