import json
import time

import requests
import os

base_url = 'http://www.yuanjingio.com'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}
try:
    r = requests.get(base_url,headers=header)
except:
    r = requests.get(base_url)
print(r.cookies)
print(r.history)
redict = r.history
for info in r.history:
    print(info.cookies)
