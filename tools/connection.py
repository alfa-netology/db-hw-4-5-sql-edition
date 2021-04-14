import sqlalchemy

def create():
    with open('./data/connection_settings') as file:
        connection_settings = file.readline()

    dbase = connection_settings
    engine = sqlalchemy.create_engine(dbase)
    connection = engine.connect()
    return connection
