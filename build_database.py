import os
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy import text
from opencdms.provider.opencdmsdb import mapper_registry

UID = os.environ["POSTGRES_USER"]
PWD = os.environ["POSTGRES_PASSWORD"]
DBNAME = os.environ["POSTGRES_DB"]
DBHOST = os.environ["POSTGRES_HOST"]
DBPORT = os.environ["POSTGRES_PORT"]

CLEAN = True

if CLEAN:
    engine = create_engine(f"postgresql+psycopg2://{UID}:{PWD}@{DBHOST}:{DBPORT}/{DBNAME}")
    if database_exists(engine.url):
        drop_database(engine.url)
    create_database(engine.url)


# ToDo update to SQLAlchemy v2 (breaking changes between 1.4 and 2)
with engine.connect() as conn:
    # Create schema
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS cdm"))
    # Add PostGIS extension
    conn.execute(text("CREATE EXTENSION Postgis;"))
    # create tables
    mapper_registry.metadata.create_all(conn)