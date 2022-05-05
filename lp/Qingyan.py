# import requests
# response=requests.get('http://www.baidu.com')
# if response.status_code != requests.status_codes.ok:
#     print('404')
# else:
#     print('200')
#
# response=requests.get('')
# files={'files':open('test.jpg')}
import requests
url='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
r=requests.get(url)
print(r.content)
with open('./baidu.png','wb') as f:
    f.write(r.content)

#响应对象
