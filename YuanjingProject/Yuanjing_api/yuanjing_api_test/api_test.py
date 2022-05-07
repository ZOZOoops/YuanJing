import json
import logging
import os.path
import re
import http.cookiejar as HC
import time
import unittest

import XTestRunner
import  requests
import  requests.utils
import urllib3
from XTestRunner import HTMLTestRunner

urllib3.disable_warnings()

class Yuanjing(object):

    def __init__(self):
        self.url = 'https://home.pre-console.gamenow.club'

    def yuanjing_api(self):
        logging.captureWarnings(True)
        url = self.url + '/index'
        headers = {'Connection':'close',
                   'Content-Type':'application/json',
                   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
                   }
        session = requests.session() # 创建session对象

        # 实例化response
        response = session.get(url, headers=headers)
        print(f'response响应头信息：{response.headers}')

        try:
            with open('./lp.txt','wb+') as f:
                f.write(response.content)
            if not os.path.isdir('./lp.txt'):
                os.mkdir('./lp/txt')
        except Exception:
            print(Exception)


        # 存储BucSso
        BucSso = f'{session.cookies["BucSsoJSESSIONID"]}'


        # 墨子登录重定向的历史地址 为一个列表
        redisList = response.history
        print(f'获取重定向的历史记录：{redisList}')
        print(f'获取第一次重定向的头部信息:{redisList[0].headers}')
        print(f'获取第一次重定向的cookie信息:{redisList[0].cookies}')
        cookies_dict = requests.utils.dict_from_cookiejar(response.cookies)
        print(f'cookie的值为：{cookies_dict}')
        print('=' * 100)
        print(f'获取第二次重定向的头部信息:{redisList[1].headers}')
        print(f'获取第二次重定向的cookie信息:{redisList[1].cookies}')
        print(f'获取第二次重定向的raw:{redisList[1]}')
        print(f'获取重定向最终的url:{redisList[1].url}')
        back_url = session.get(redisList[1].url)
        print()


        print('当前头部信息为：{}'.format(response.headers))

        # try:
        #     assert response.status_code == 200
        #     print('状态码断言成功')
        # except:
        #     print('status_code断言失败,当前状态码为{}'.format(response.status_code))

        redirect_url = redisList[1].url

        cookie = {
            'Cookie':BucSso
        }
        data = {
            'account':'13132221817',
            'password':'Liu123123'
        }
        data = json.dumps(data)
        login_api = session.post(redirect_url,data=data,cookies=cookie)
        print(login_api)


    def login(self):
        pass
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':

    a = Yuanjing()
    a.yuanjing_api()

    now = time.strftime('%Y-%m-%d_%H：%M：%S')
    file_name =  '../report/' + now + '_test_result.html'
    print(os.getcwd())

    with open(file_name,'wb') as f:


        runner = HTMLTestRunner(
            stream= f,
            title='接口测试报告',
            description='用例执行情况',
            language='zh-CN'
        )
        runner.run(discover)

