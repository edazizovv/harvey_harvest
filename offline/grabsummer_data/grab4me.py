#


#
import pandas


#


#

d_source = '../dataset_grouped.csv'
d_add_funds_aum = './funds_aum.csv'
d_add_metals = './metals.csv'

source = pandas.read_csv(d_source)
source['Timestamp'] = pandas.to_datetime(source['Timestamp'])
source = source.set_index('Timestamp')

metals = pandas.read_csv(d_add_metals)
metals['Timestamp'] = pandas.to_datetime(metals['Timestamp'])
metals = metals.set_index('Timestamp')

funds_aum = pandas.read_csv(d_add_funds_aum)
funds_aum['Timestamp'] = pandas.to_datetime(funds_aum['Timestamp'])
funds_aum = funds_aum.set_index('Timestamp')
joint = source.merge(right=funds_aum, left_index=True, right_index=True, how='left')
joint = joint.merge(right=metals, left_index=True, right_index=True, how='left')

__ff = joint.copy()

funds_nonna_mask = ~pandas.isna(joint).any(axis=1)
start, end = joint.loc[funds_nonna_mask, :].index.min(), joint.loc[funds_nonna_mask, :].index.max()
joint = joint.loc[(joint.index >= start) * (joint.index <= end), :]
joint = joint.fillna(method='ffill')

