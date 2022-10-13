# Machine learning

The `machine_learning` folder contains python scripts both for fetching data from the analytics platform and also scripts for machine learning (training of model, prediction).

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
export GOODDATA_HOST=<gooddata-uri>
export GOODDATA_TOKEN=<gooddata-api-token>
export WORKSPACE_ID=<workspace-id>
export INSIGHT_ID=<insight-id>
```

### Install dependencies

```bash
$ pip install -r requirements.txt
```

### Run scripts

If you want to fetch data, just run:

```bash
$ python gooddata_data_fetch.py
```

The similar approach applies also for other scripts. 

Note: you have to first run `train_model.py` to successfully run `prediction.py`.

## Troubleshooting 

The whole project was built on macOS. It is possible that it will not be working on other systems.

It may fail import some libraries, try to install `libomp`:

```bash
$ brew install libomp 
```
