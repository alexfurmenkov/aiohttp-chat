import peewee_async
from src.db_data import database
import src.models as models


database.connect()

for model in map(models.__dict__.get, models.__all__):
    database.create_tables([model])

database.close()
objects = peewee_async.Manager(database)
