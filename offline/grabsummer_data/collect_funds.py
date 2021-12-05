
import os
import requests
import pandas


def symbol_to_number(x):
    if 'B' in x:
        x = x.replace('B', '')
        x = float(x) * 1000
        return x
    elif 'M' in x:
        x = x.replace('M', '')
        x = float(x)
        return x
    else:
        raise Exception("idk what this means: {0}".format(x))


btc = []
for file in [x for x in os.listdir('./raw/gbtc/') if 'GBTC' in x]:
    snip = pandas.read_csv('./raw/gbtc/' + file)
    snip = snip.drop(columns='Unnamed: 0')
    snip = snip.rename(columns={x: x.replace(' ', '') for x in snip.columns.values})
    btc.append(snip)
btc = pandas.concat(btc, axis=0)
btc['Date'] = pandas.to_datetime(btc['Date'])
btc['Value'] = btc['Value'].str.replace(' ', '')
btc['Value'] = btc['Value'].apply(func=symbol_to_number)
btc = btc.rename(columns={'Date': 'Timestamp', 'Value': 'GBTC AUM'})
btc = btc.set_index('Timestamp')

eth = []
for file in [x for x in os.listdir('./raw/ethe/') if 'ETHE' in x]:
    snip = pandas.read_csv('./raw/ethe/' + file)
    snip = snip.drop(columns='Unnamed: 0')
    snip = snip.rename(columns={x: x.replace(' ', '') for x in snip.columns.values})
    eth.append(snip)
eth = pandas.concat(eth, axis=0)
eth['Date'] = pandas.to_datetime(eth['Date'])
eth['Value'] = eth['Value'].str.replace(' ', '')
eth['Value'] = eth['Value'].apply(func=symbol_to_number)
eth = eth.rename(columns={'Date': 'Timestamp', 'Value': 'ETHE AUM'})
eth = eth.set_index('Timestamp')

joint = btc.merge(right=eth, left_index=True, right_index=True, how='inner')
joint = joint.sort_index()
joint.to_csv('./funds_aum.csv')

"""
n = 'ETHE_6b'
data = pandas.read_clipboard()
data.to_csv('./raw/ethe/{0}.csv'.format(n))
print(data)
"""


# https://ycharts.com/companies/GBTC/total_assets_under_management

