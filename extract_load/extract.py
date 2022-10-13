import http.client
import json
import os

token = os.environ["RAPID_API_TOKEN"]
stock_symbol = os.environ["STOCK_SYMBOL"]
conn = http.client.HTTPSConnection("meteostat.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "4fc37563d6msh7b9fb7f0417a5f4p1caa4ejsnf36924701105",
    'X-RapidAPI-Host': "alpha-vantage.p.rapidapi.com"
}

conn.request(
    "GET",
    f"/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&outputsize=compact&datatype=json",
    headers=headers
)


def get_data():
    stock_data = {}
    try:
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        data_json = json.loads(data)
        conn.close()
        stock_data["symbol"] = data_json["Meta Data"]["2. Symbol"]
        stock_data["data"] = data_json["Time Series (Daily)"]
    except:
        print("extract operation has failed")

    return stock_data
