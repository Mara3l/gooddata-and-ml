# Machine learning

The `extract_load` folder contains python scripts to extract and load data into the database.

The data is extracted from the [Meteostat API](https://rapidapi.com/meteostat/api/meteostat).

## Getting started

### Setup virtual environment

Set up a virtual environment:

**Create virtual environment**:

```bash
$ virtualenv venv
```

**Activate virtual environment**:

```bash
$ source venv/bin/activate
```

You should see a `(venv)` appear at the beginning of your terminal prompt indicating that you are working inside the `virtualenv`.

**Leave virtual environment run**:

```bash
$ deactivate
```

### Setup env variable in virtual environments

```bash
export RAPID_API_TOKEN=<gooddata-uri>
export WEATHER_STATION_ID=<wather-station-id>
export DATE_FROM=<date-from>
export DATE_TO=<date-to>
export POSTGRES_HOST=<postgres-host>
export POSTGRES_PORT=<postgres-port>
export POSTGRES_USER=<postgres-user>
export POSTGRES_PASS=<postgres-password>
export POSTGRES_DBNAME=<postgres-dbname>
export POSTGRES_INPUT_SCHEMA=<input-stage-schema>
```

### Install dependencies

```bash
$ pip install -r requirements.txt
```

### Run scripts

If you want to extract and load data, just run:

```bash
$ python main.py
```
