import pandas as pd
import datetime

#reading bitcoin data
btc_data = pd.read_csv('bitcoin_ohlcv.csv')

#dropping irrevelent columns
btc_data =btc_data.drop(columns=['SNo','Name','Symbol'])

#renaming date column
btc_data = btc_data.rename(columns={'Date': 'date'})

#converting date type object to datetime
exchange_data = btc_data.assign(date=pd.to_datetime(btc_data['date']))

##
start_date="2016-01-01"
end_date="2021-01-02"
data = exchange_data
data = exchange_data.reset_index()
data = exchange_data
data = data.drop(data[data['date'] < start_date].index)
data = data.drop(data[data['date'] > end_date].index)
data = data.reset_index(drop=True)

exchange_data = data

print('converted object to datetime format')

print(exchange_data.head())
print(exchange_data.tail())

exchange_data.to_csv('exchange_data.csv')