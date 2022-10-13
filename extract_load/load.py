import os

import psycopg2
from psycopg2.extras import Json
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

host = os.getenv('POSTGRES_HOST', 'localhost')
port = os.getenv('POSTGRES_PORT', 5432)
user = os.getenv('POSTGRES_USER', 'postgres')
password = os.getenv('POSTGRES_PASS')
name = os.getenv('POSTGRES_DBNAME')
schema = os.getenv('POSTGRES_INPUT_SCHEMA', 'public')

conn = psycopg2.connect(
    user=user,
    password=password,
    host=host,
    port=port,
    database=name
)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)


def load_data(stock_data):
    loaded = False
    try:
        cur = conn.cursor()
        cur.execute(
            """
            create table if not exists input_stage.stock(
                id serial,
                symbol varchar,
                date date,
                data jsonb
            )
            """
        )
        for item in stock_data["data"]:
            print(stock_data["data"][item])
            cur.execute(
                "insert into input_stage.stock(symbol, date, data) values (%s, %s, %s)",
                [
                    stock_data["symbol"],
                    item,
                    Json(stock_data["data"][item])
                ]
            )
        conn.commit()
        conn.close()
        loaded = True
    except:
        print("load operation has failed")
    return loaded
