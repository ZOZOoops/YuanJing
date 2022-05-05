import json
import requests

# url = 'www.cloudgametools.com/'
# headers = {'ContentType':'Application/Json'}

r = requests.get('https://www.baidu.com')
# 等待时间失去响应
print(r.url)
