#
import pandas


#
listed = ['BTC', 'ETH', 'DOGE', 'LTC', 'XRP']
excluded = []


def rename(x):
    if 'open' in x:
        return x.replace('open', 'Open')
    if 'close' in x:
        return x.replace('close', 'Close')
    if 'high' in x:
        return x.replace('high', 'High')
    if 'low' in x:
        return x.replace('low', 'Low')
    if 'volume' in x:
        return x.replace('volume', 'Volume')


data = []
for li in listed:
    d = './raw/crypto/{0}-USDT.parquet'.format(li)
    data_ = pandas.read_parquet(d)
    data_.index = data_.index.rename(name='Timestamp')
    data_ = data_.drop(columns=[x for x in data_.columns.values if x not in ['open', 'low', 'high', 'close', 'volume']])
    data_ = data_.rename(columns={x: '{0}-{1}_{2}'.format(li, 'USD', x) for x in data_.columns.values if x not in excluded})
    data.append(data_)

data_crypto = pandas.concat(data, axis=1)
data_crypto = data_crypto[[x for x in data_crypto.columns.values if any(j in x for j in ['open', 'close', 'high', 'low', 'volume'])]].copy()
data_crypto = data_crypto.rename(columns={x: rename(x) for x in data_crypto.columns.values})

listed = {'EUR': ['DAT_XLSX_EURUSD_M1_2017',
                  'DAT_XLSX_EURUSD_M1_2018',
                  'DAT_XLSX_EURUSD_M1_2019',
                  'DAT_XLSX_EURUSD_M1_202001',
                  'DAT_XLSX_EURUSD_M1_202002',
                  'DAT_XLSX_EURUSD_M1_202003',
                  'DAT_XLSX_EURUSD_M1_202004',
                  'DAT_XLSX_EURUSD_M1_202005',
                  'DAT_XLSX_EURUSD_M1_202006',
                  'DAT_XLSX_EURUSD_M1_202007',
                  'DAT_XLSX_EURUSD_M1_202008',
                  'DAT_XLSX_EURUSD_M1_202009',
                  'DAT_XLSX_EURUSD_M1_202010',
                  'DAT_XLSX_EURUSD_M1_202011',
                  'DAT_XLSX_EURUSD_M1_202012'],
          'JPY': ['DAT_XLSX_USDJPY_M1_2017',
                  'DAT_XLSX_USDJPY_M1_2018',
                  'DAT_XLSX_USDJPY_M1_2019',
                  'DAT_XLSX_USDJPY_M1_202001',
                  'DAT_XLSX_USDJPY_M1_202002',
                  'DAT_XLSX_USDJPY_M1_202003',
                  'DAT_XLSX_USDJPY_M1_202004',
                  'DAT_XLSX_USDJPY_M1_202005',
                  'DAT_XLSX_USDJPY_M1_202006',
                  'DAT_XLSX_USDJPY_M1_202007',
                  'DAT_XLSX_USDJPY_M1_202008',
                  'DAT_XLSX_USDJPY_M1_202009',
                  'DAT_XLSX_USDJPY_M1_202010',
                  'DAT_XLSX_USDJPY_M1_202011',
                  'DAT_XLSX_USDJPY_M1_202012']}

data_eur = []
for li in listed['EUR']:
    print(li)
    d = './raw/fiat/{0}.xlsx'.format(li)
    data_ = pandas.read_excel(d, header=None, names=['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])
    data_ = data_.set_index('Timestamp')
    data_ = data_.rename(columns={x: 'EUR-USD_{0}'.format(x) for x in data_.columns.values if x not in excluded})
    data_eur.append(data_)
data_eur_ = pandas.concat(data_eur, axis=0)
data_eur_ = data_eur_.drop_duplicates()

data_jpy = []
for li in listed['JPY']:
    print(li)
    d = './raw/fiat/{0}.xlsx'.format(li)
    data_ = pandas.read_excel(d, header=None, names=['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])
    data_ = data_.set_index('Timestamp')
    for c in ['Open', 'High', 'Low', 'Close']:
        data_[c] = 1 / data_[c]
    data_ = data_.rename(columns={x: 'JPY-USD_{0}'.format(x) for x in data_.columns.values if x not in excluded})
    data_jpy.append(data_)
data_jpy_ = pandas.concat(data_jpy, axis=0)
data_jpy_ = data_jpy_.drop_duplicates()

data_all = pandas.concat((data_crypto, data_eur_, data_jpy_), axis=1)
data_all = data_all.fillna(method='ffill')
data_all = data_all.dropna()

# data_all.to_csv('../dataset.csv')
