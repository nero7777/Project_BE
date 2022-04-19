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

exchange_data = pd.read_csv('exchange_data.csv')
exchange_data = exchange_data.iloc[: , 1:]
print(exchange_data.head())

blockchain_data = pd.read_csv('blockchain_data.csv')
blockchain_data = blockchain_data.iloc[: , 1:]
print(blockchain_data.head())

macro_econ_data = pd.read_csv('macro_econ_data.csv')
macro_econ_data = macro_econ_data.iloc[: , 1:]
print(macro_econ_data.head())

sentiment_data = pd.read_csv('sentiment_data.csv')
sentiment_data = sentiment_data.iloc[: , 1:]
print(sentiment_data.head())

#####################################################Merging datasets one by one
model_data = exchange_data.merge(blockchain_data,on='date',how='inner')
print(model_data.head())
model_data = model_data.merge(macro_econ_data,on='date',how='inner')
print(model_data.head())
model_data = model_data.merge(sentiment_data,on='date',how='inner')
print(model_data.head())

model_data.to_csv('model_data.csv')
