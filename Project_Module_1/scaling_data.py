import numpy as np
import pandas as pd
from sklearn.preprocessing import minmax_scale

model_data = pd.read_csv('model_data.csv')
model_data = model_data.iloc[: , 1:]
model_data.rename(columns={'date': 'date', 'Open*': 'btc_open', 'High': 'btc_high', 'Low': 'btc_low', \
                                    'Close': 'btc_close', 'Volume': 'btc_volume', \
                                    'Marketcap': 'btc_market_cap','avg_block_size':'bch_avg_block_size',\
                                    'transactions':'bch_transactions','mining_revenue':'bch_mining_revenue',\
                                    'accounts':'bch_accounts','google_trends_btc':'google_trends_bitcoin'}, inplace=True)
model_data=model_data.drop(columns=['btc_low','Open'])
imputed_df = model_data


imputed_df[['btc_high', 'btc_close', 'btc_volume', 'btc_market_cap', \
       'bch_avg_block_size', 'bch_transactions', 'bch_mining_revenue', \
       'bch_accounts', 'sp_close', 'dj_close', 'google_trends_bitcoin']] = \
        minmax_scale(imputed_df[['btc_high', 'btc_close', 'btc_volume', \
                                 'btc_market_cap', 'bch_avg_block_size', \
                                 'bch_transactions', 'bch_mining_revenue', 'bch_accounts', 'sp_close', 'dj_close', 'google_trends_bitcoin']])

imputed_df['date'] = model_data['date']

imputed_df["date"] = imputed_df["date"].values[::1]

model_data_latest=imputed_df

print(model_data_latest.head())
model_data_latest.to_csv('model_data_scaled.csv')