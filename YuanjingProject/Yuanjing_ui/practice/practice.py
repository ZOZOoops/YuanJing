#-*- coding:utf-8 -*-
import unittest
import time
from selenium import webdriver
from threading import Thread  #导入python多线程模块
def test1(browser,url):
    driver = None
    # 你可以自定义这里，添加更多浏览器支持进来
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
    elif browser == 'Edge':
        driver = webdriver.Edge()
    if driver == None:
        exit()
        # raise Exception('当前没有浏览器可以使用')
    print ("开始")
    driver.get(url)
    print(driver.current_url)
    print ("清除数据")
    driver.find_element_by_id('kw').clear()
    driver.find_element_by_id('kw').send_keys('MTbaby')
    driver.find_element_by_id('su').click()
    time.sleep(5)
    #关闭浏览器
    driver.quit()


if __name__=="__main__":
    #浏览器好额首页url
    date = {
        'edge':'http://www.baidu.com',
        'Firefox':'http://www.baidu.com',
        'Chrome':'http://www.baidu.com'
    }
    #构建线程
    thresds = []
    for b,url in date.items():
        t = Thread(target=test1,args=(b,url))
        thresds.append(t)
    #启动所有线程
    for s in thresds:
        s.start()
