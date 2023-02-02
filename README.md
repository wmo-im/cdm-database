# CDM Database

This repository contains a minimal set of docker images for building a database to 
contain data in the CDM data model.

- _wmo-im-opencdms-database_: image / container for timescaledb 
- _wmo-im-opencdms-cli_: imge / container for running python etc.

# Usage

```bash
docker-compose build # build the containers if required
docker-compose up -d # start up the containers
docker exec -it wmo-im-opencdms-cli bash # enter bash shell
cd /local/app # change directory to location of code
python3 build_database.py # now build the database and ingest sample data
```

- Connection parameters are stored in the _default.env_ file.
- Test data can be found in the [data directory](https://github.com/wmo-im/cdm-database/tree/main/data)

# Data source + licensing

Data have been extracted and transformed from the Environment and Climate Change Canada (ECCC) [GeoMet-OGC-API service.](https://api.weather.gc.ca/)

## Data sets

- [ECCC Climate Stations](https://api.weather.gc.ca/collections/climate-stations)
- [Hourly climate observations](https://api.weather.gc.ca/collections/climate-hourly)

## License

Please see https://eccc-msc.github.io/open-data/licence/readme_en/ for information on the licensing and usage permissions.
