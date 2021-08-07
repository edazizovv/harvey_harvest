#
import numpy
import pandas
import datetime

#


#
# BOSS OF THE QUANTILE


def q(n):
    def q_(x):
        return numpy.quantile(x, n)
    q_.__name__ = 'quantile_{0}'.format(n)
    return q_


d = './dataset.csv'
data = pandas.read_csv(d)
data['Timestamp'] = pandas.to_datetime(data['Timestamp'])
data['Timestamp'] = data['Timestamp'] + pandas.tseries.offsets.DateOffset(hours=18)
data = data.set_index('Timestamp')
data = data[[x for x in data.columns.values if 'Close' in x]].copy()

data['year'] = data.index.year
data['month'] = data.index.month
data['day'] = data.index.day
"""
data_grouped = data.groupby(by=['year', 'month', 'day']).agg(
    func=[q(0.01), q(0.10), q(0.50), q(0.90), q(0.99)])

data_grouped.columns = ['||'.join(col).strip() for col in data_grouped.columns.values]

data_grouped = data_grouped.reset_index()
data_grouped[['year', 'month', 'day']] = data_grouped[['year', 'month', 'day']].astype(dtype=numpy.int64)
data_grouped['Timestamp'] = data_grouped.apply(func=lambda x: datetime.date(int(x['year']), int(x['month']), int(x['day'])), axis=1)
data_grouped = data_grouped.drop(columns=['year', 'month', 'day'])
data_grouped = data_grouped.set_index('Timestamp')

data_grouped.to_csv('./dataset_grouped.csv')
"""

# BOSS OF THE CLASSY
"""

def q(n):
    def q_(x):
        return numpy.quantile(x, n)
    q_.__name__ = 'quantile_{0}'.format(n)
    return q_


d = './dataset.csv'
data = pandas.read_csv(d)
data['Timestamp'] = pandas.to_datetime(data['Timestamp'])
data['Timestamp'] = data['Timestamp'] + pandas.tseries.offsets.DateOffset(hours=18)
data = data.set_index('Timestamp')
data = data[[x for x in data.columns.values if 'Close' in x]].copy()

targets = data.columns.values

data['year'] = data.index.year
data['month'] = data.index.month
data['day'] = data.index.day

data_grouped = data.groupby(by=['year', 'month', 'day']).agg(
    func=[q(0.50)])

data_grouped.columns = ['||'.join(col).strip() for col in data_grouped.columns.values]

data = data.reset_index()
data = data.merge(right=data_grouped, left_on=['year', 'month', 'day'], right_on=['year', 'month', 'day'], how='left')
data = data.set_index('Timestamp')

data = data[(data.index.hour == 0) * (data.index.minute == 0) * (data.index.second == 0)]

for target in targets:
    data['{0}__UP0.50'.format(target)] = data.apply(func=lambda x: x[target] < x['{0}||quantile_0.5'.format(target)], axis=1)
    data['{0}__UP0.50'.format(target)] = data['{0}__UP0.50'.format(target)].astype(dtype=numpy.int64)

data = data.drop(columns=['year', 'month', 'day'])

data.to_csv('./dataset_classified.csv')
"""