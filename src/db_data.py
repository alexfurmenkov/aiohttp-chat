import peewee_async

DATABASE_NAME = 'aiochat'
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = 'postgres'
DATABASE_HOST = 'localhost'
DATABASE_PORT = 5432

database = peewee_async.PostgresqlDatabase(database=DATABASE_NAME,
                                           user=DATABASE_USER,
                                           password=DATABASE_PASSWORD,
                                           host=DATABASE_HOST,
                                           port=DATABASE_PORT)
