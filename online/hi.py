
import datetime
import time
import urllib3





start_date = datetime.datetime(2019, 1, 1)
end_date = datetime.datetime(2020, 1, 1)


http = urllib3.PoolManager()
"""
r = http.request('POST', 'https://www.binance.com/fapi/v1/continuousKlines?pair={0}&contractType={1}&interval={2}&startTime={3}&endTime={4}'.format(
    'BTC-USD',
'CURRENT_MONTH',
'MINUTE',
time.mktime(start_date.timetuple())*1e3 + start_date.microsecond/1e3,
time.mktime(end_date.timetuple())*1e3 + end_date.microsecond/1e3),
                 headers={'Content-Type': 'application/json'})
"""

r = http.request('GET', "https://fapi.binance.com/fapi/v1/continuousKlines?pair={0}&contractType={1}&interval={2}&startTime={3}&endTime={4}&limit={5}".format(
    'BTCUSDT',
'NEXT_QUARTER',
'1M',
time.mktime(start_date.timetuple())*1e3 + start_date.microsecond/1e3,
time.mktime(end_date.timetuple())*1e3 + end_date.microsecond/1e3,
1500),
                 headers={'Content-Type': 'application/json'})

