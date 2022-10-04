# Data transformation

The `data_transformation` folder contains the dbt tool that is responsible for loading and transforming data.

The folder `seeds` is the CSV file `card_transdata.csv` that contains demo data. Firstly, dbt loads demo data into the database and then transforms it.

If you want to learn more about dbt, I encourage you to read the [documentation](https://docs.getdbt.com/).

## Before you start

In order to successfully run dbt, you have to set up correct database credentials in `/.dbt/profiles.yml`.

## Getting started

### Seed data

The following command loads data into the database schema `input_stage`:

```bash
$ dbt seed --full-refresh
```

### Run dbt

The following command transforms data into the database schema `output_stage`:

```dbt
$ dbt run
```
