import seaborn as sns
import datetime
import matplotlib.pyplot as plt
import urllib.request as urllib
import time
import numpy as np
import pandas as pd
from datetime import timedelta
import numpy as np
import requests
import csv
import json
from pytrends.request import TrendReq


#function to drop intial rows for blockchain data as gathering the data on timeframe = "all time"
def drop_initial_rows(api, new_col_name, start_date="2016-01-01"):
    # Read data
    api_range_format = api
    data = pd.read_csv(urllib.urlopen(api_range_format))

    data = pd.DataFrame(data.values, columns=['date', new_col_name])

    data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')

    data['date'] = pd.DataFrame(data=data['date'], columns=['date'])

    data['date'] = pd.to_datetime(data['date'])

    # Some time series from blockchain.com calculate the data every 3 days and not every day
    # In the dataset, if there is a date where there's no value, setting the value of the day before
    data = data.set_index('date').resample('D').ffill()

    # Reset index
    data.index.name = 'date'
    data = data.reset_index()
    data = data
    data = data.drop(data[data['date'] < start_date].index)
    data = data.reset_index(drop=True)

    return data

#function v2 to drop intial rows for blockchain avg size data as gathering the data on timeframe = "all time"
def drop_initial_rowsv2(api, new_col_name, start_date="2016-01-01"):
    # Read data

    data = api
    data = pd.DataFrame(data.values, columns=['date', new_col_name])

    data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')

    data['date'] = pd.DataFrame(data=data['date'], columns=['date'])

    data['date'] = pd.to_datetime(data['date'])

    #for missing values
    data = data.set_index('date').resample('D').ffill()

    # Reset index
    data.index.name = 'date'
    data = data.reset_index()
    data = data
    data = data.drop(data[data['date'] < start_date].index)
    data = data.reset_index(drop=True)

    return data


#feature 1 (avg_block_size)
block_size_api = pd.read_csv('avg_block_size.csv')
avg_block_size_data = drop_initial_rowsv2(block_size_api, 'avg_block_size')

#feature 2 (num_transactions)
txs_api = "https://api.blockchain.info/charts/n-transactions?timespan=all&format=csv"
txs_data = drop_initial_rows(txs_api, 'transactions')

#feature 3 (bch_min_rev)
bchain_mirev_api = "https://www.quandl.com/api/v3/datasets/BCHAIN/MIREV.csv?api_key=55AcwGQK3qwgy8J3K4Pw"
bchain_mirev_data = drop_initial_rows(bchain_mirev_api, "mining_revenue")

#feature 4 (bch_num_acc)
bch_accounts_api = "https://api.blockchain.info/charts/my-wallet-n-users?timespan=all&format=csv"
bch_accounts_data = drop_initial_rows(bch_accounts_api, 'accounts')

blockchain_data = avg_block_size_data.merge(txs_data, on='date', how='inner').merge(bchain_mirev_data, on='date', how='inner').merge(bch_accounts_data, on='date', how='inner')

#converting date type object to datetime
blockchain_data = blockchain_data.assign(date=pd.to_datetime(blockchain_data['date']))

##
start_date="2016-01-01"
end_date="2021-01-01"
data = blockchain_data
data = blockchain_data.reset_index()
data = blockchain_data
data = data.drop(data[data['date'] < start_date].index)
data = data.drop(data[data['date'] > end_date].index)
data = data.reset_index(drop=True)

blockchain_data = data

print(blockchain_data.head())
print(blockchain_data.tail())

blockchain_data.to_csv('blockchain_data.csv')