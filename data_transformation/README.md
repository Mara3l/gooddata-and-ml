# Data transformation

The `data_transformation` folder contains the dbt tool that is responsible for transforming data.

If you want to learn more about dbt, I encourage you to read the [documentation](https://docs.getdbt.com/).

## Before you start

In order to successfully run dbt, you have to set up correct database credentials in `/.dbt/profiles.yml`.

## Getting started

The prerequisite is to have data loaded in the database schema `input_stage`. If you do not have, please check the `extract_load` folder.

### Run dbt

The following command transforms data into the database schema `output_stage`:

```dbt
$ dbt run
```
