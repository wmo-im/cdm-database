import os
from sqlalchemy import create_engine, text
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.orm import sessionmaker

from opencdms.provider import opencdmsdb

# set connection details
UID = os.environ["POSTGRES_USER"]
PWD = os.environ["POSTGRES_PASSWORD"]
DBNAME = os.environ["POSTGRES_DB"]
DBHOST = os.environ["POSTGRES_HOST"]
DBPORT = os.environ["POSTGRES_PORT"]

engine = create_engine(f"postgresql+psycopg2://{UID}:{PWD}@{DBHOST}:{DBPORT}/{DBNAME}")
# check whether we want to start clean
CLEAN = True
if CLEAN:
    if database_exists(engine.url):
        drop_database(engine.url)
    create_database(engine.url)

with engine.begin() as conn:
    # Create schema
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS cdm"))
    # Add PostGIS extension
    conn.execute(text("CREATE EXTENSION Postgis;"))

# create tables
opencdmsdb.mapper_registry.metadata.create_all(engine)

opencdmsdb.start_mappers()

session = sessionmaker(bind=engine)()
cursor = session.connection().connection.cursor()

code_tables = {
    "cdm.observation_type": "observation_type.csv",
    "cdm.observed_property": "observed_property.csv",
    "cdm.observing_procedure": "observing_procedure.csv",
    "cdm.users": "users.csv",
    "cdm.record_status": "status.csv",
    "cdm.hosts": "stations.csv",
    "cdm.source": "source.csv",
}

data_tables = {
    "cdm.observations": ["CA_6016975_1953.csv"]
}

for key, value in code_tables.items():
    with open(f"/local/app/data/code_tables/{value}") as fh:
        cursor.copy_expert(f"COPY {key} FROM STDIN WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA'", fh)

for key, value in data_tables.items():
    if isinstance(value, list):
        for item in value:
            with open(f"/local/app/data/data_tables/{item}") as fh:
                cursor.copy_expert(f"COPY {key} FROM STDIN WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA'", fh)
    else:
        with open(f"/local/app/data/data_tables/{value}") as fh:
            cursor.copy_expert(f"COPY {key} FROM STDIN WITH CSV HEADER DELIMITER AS '|' NULL AS 'NA'", fh)

session.commit()
session.close()

