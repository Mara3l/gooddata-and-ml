from extract import get_data
from load import load_data

weather_data = get_data()

if bool(weather_data):
    load_data(weather_data)

print('DONE')
