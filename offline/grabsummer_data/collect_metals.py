#
import os


#
import pandas


#


#
files = [x for x in os.listdir('./raw/metal/')]

gold = pandas.read_excel('./raw/metal/' + [x for x in files if 'gold' in x][0])
silver = pandas.read_excel('./raw/metal/' + [x for x in files if 'silver' in x][0])
platinum = pandas.read_excel('./raw/metal/' + [x for x in files if 'platinum' in x][0])
palladium = pandas.read_excel('./raw/metal/' + [x for x in files if 'palladium' in x][0])

gold['Timestamp'] = pandas.to_datetime(gold['Timestamp'])
silver['Timestamp'] = pandas.to_datetime(silver['Timestamp'])
platinum['Timestamp'] = pandas.to_datetime(platinum['Timestamp'])
palladium['Timestamp'] = pandas.to_datetime(palladium['Timestamp'])

gold = gold.set_index('Timestamp')
silver = silver.set_index('Timestamp')
platinum = platinum.set_index('Timestamp')
palladium = palladium.set_index('Timestamp')

metals = gold.merge(right=silver, left_index=True, right_index=True, how='outer')
metals = metals.merge(right=platinum, left_index=True, right_index=True, how='outer')
metals = metals.merge(right=palladium, left_index=True, right_index=True, how='outer')


metals.to_csv('./metals.csv')
