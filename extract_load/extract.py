import http.client
import json
import os

token = os.environ["RAPID_API_TOKEN"]
station_id = os.environ["WEATHER_STATION_ID"]
data_from = os.environ["DATE_FROM"]
data_to = os.environ["DATE_TO"]
conn = http.client.HTTPSConnection("meteostat.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': token,
    'X-RapidAPI-Host': "meteostat.p.rapidapi.com"
}

conn.request(
    "GET",
    f"/stations/daily?station={station_id}&start={data_from}&end={data_to}",
    headers=headers
)


def get_data():
    weather_data = {}
    try:
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        conn.close()
        weather_data = json.loads(data)["data"]
    except:
        print("extract operation has failed")

    return weather_data
