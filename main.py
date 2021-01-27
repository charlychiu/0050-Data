import requests
import json
import time
import os

my_headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15'}
count = 0
for y in range(2010, 2021):
  if not os.path.exists('history/' + str(y)):
    os.makedirs('history/' + str(y))
  for m in range(1, 13):
    filename = "{0}{1:0>2d}01".format(y, m)
    r = requests.get('https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&stockNo=0050&date=' + filename, headers=my_headers)
    with open('history/' + str(y) + '/' + filename + '.json', 'w') as outfile:
      json.dump(r.json(), outfile)
    time.sleep(2)
    print(filename)
    count += 1