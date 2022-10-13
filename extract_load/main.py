from extract import get_data
from load import load_data

stock_data = get_data()

if bool(stock_data):
    load_data(stock_data)

print('DONE')
