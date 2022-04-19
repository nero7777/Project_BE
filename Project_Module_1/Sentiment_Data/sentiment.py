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

"""
pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["bitcoin"]
pytrends.build_payload(kw_list, timeframe='2016-1-1 2021-1-1', geo='', gprop='')
sentiment_data = pytrends.interest_over_time()

sentiment_data = sentiment_data.drop(columns=['isPartial'])

sentiment_data.to_csv('sentiment_data.csv')
"""
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

sentimentdata = pd.read_csv('sentiment_data.csv')

sentiment_data = drop_initial_rowsv2(sentimentdata,'google_trends_btc')


print(sentiment_data.head())
print(sentiment_data.tail())

sentiment_data.to_csv('sentiment_data.csv')



