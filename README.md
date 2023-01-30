# CDM Database

This repository contains a minimal set of docker images for building a database to 
contain data in the CDM data model.

- _wmo-im-opencdms-database_: image / container for timescaledb 
- _wmo-im-opencdms-cli_: imge / container for running python etc.

# Usage

```bash
docker-compose build # build the containers if requried
docker-compose up -d # start up the containers
docker exec -it wmo-im-opencdms-cli bash # enter bash shell
cd /local/app # change directory to location of code
python3 build_database.py # now build the database
```

- Connection parameters are stored in the _default.env_ file.
- Prior to running paths will need to be updated in the _docker-compose-yml_.
- Test data can be found in the _cdm_ branch of the [OpenCDMS test data repository](https://github.com/opencdms/opencdms-test-data/tree/cdm).
