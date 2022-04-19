import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

model_data = pd.read_csv('model_data.csv')
model_data = model_data.iloc[: , 1:]

model_data.rename(columns={'date': 'date', 'Open*': 'btc_open', 'High': 'btc_high', 'Low': 'btc_low', \
                                    'Close': 'btc_close', 'Volume': 'btc_volume', \
                                    'Marketcap': 'btc_market_cap','avg_block_size':'bch_avg_block_size',\
                                    'transactions':'bch_transactions','mining_revenue':'bch_mining_revenue',\
                                    'accounts':'bch_accounts','google_trends_btc':'google_trends_bitcoin'}, inplace=True)
#model_data=model_data.drop(columns=['btc_low','Open'])

""" Ignore the date column """
all_features_df = model_data.loc[:, model_data.columns != 'date']

#
# Change in percentage =>
#    initially count: increasing = y_t - y_(t-1)
#    then: %growth = (Increase-y_(t-1))*100
corr = all_features_df.pct_change().corr(method='pearson')
fig, ax = plt.subplots(figsize=(7,5))
sns.heatmap(corr,
            xticklabels=[col.replace("_price", "") for col in corr.columns.values],
            yticklabels=[col.replace("_price", "") for col in corr.columns.values],
            annot_kws={"size": 16})
plt.show()

# Presentation in tabular form
cmap=sns.diverging_palette(220, 20, sep=20, as_cmap=True)

def magnify():
    return [dict(selector="th",
                 props=[("font-size", "7pt")]),
            dict(selector="td",
                 props=[('padding', "0em 0em")]),
            dict(selector="th:hover",
                 props=[("font-size", "12pt")]),
            dict(selector="tr:hover td:hover",
                 props=[('max-width', '200px'),
                        ('font-size', '12pt')])
]

corr.style.background_gradient(cmap, axis=1)\
    .set_properties(**{'max-width': '80px', 'font-size': '10pt'})\
    .set_caption("Hover to magify")\
    .set_precision(2)\
    .set_table_styles(magnify())
