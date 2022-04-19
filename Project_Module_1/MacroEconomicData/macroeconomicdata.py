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

def drop_initial_rowsv2(api, new_col_name, start_date="2016-01-01",end_date="2021-01-01"):
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
    data = data.drop(data[data['date'] > end_date].index)
    data = data.reset_index(drop=True)

    return data

sp_data = pd.read_csv('sp_data.csv')
sp_data = drop_initial_rowsv2(sp_data,'sp_close')
print(sp_data.head())
#sp_data.to_csv('sp_data.csv')

dj_data = pd.read_csv('dj_data.csv')
dj_data = drop_initial_rowsv2(dj_data,'dj_close')
print(dj_data.head())
#dj_data.to_csv('dj_data.csv')

macro_econ_data = sp_data.merge(dj_data,on='date',how='inner')
macro_econ_data.to_csv('macro_econ_data.csv')