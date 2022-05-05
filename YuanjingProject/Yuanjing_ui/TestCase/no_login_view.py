import configparser
import logging
import os
import unittest
import time
import XTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from Yuanjing_ui.Base.base_page import Keys
from configparser import ConfigParser


class Yuanjing_nologin_view(unittest.TestCase, Keys):

    base_url = 'https://www.yuanjingio.com/'

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.open(self.base_url)

    def tearDown(self) -> None:
        self.quit()

    # @unittest.skip
    def test_001_assert(self):
        url = self.driver.current_url
        self.assertEqual(url, self.base_url, msg='url断言错误')

    def test_002_about(self):
        # 验证未登录情况下进入到”关于我们“是否正常
        # 点击”关于我们“按钮
        self.click((By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(1)'))
        self.implicilty_wait(2)

        window_handles = self.driver.window_handles
        # 切换到最新的窗口验证url是否正确
        self.driver.switch_to_window(window_handles[-1])
        ele = self.driver.current_url
        self.assertEqual(ele,self.base_url + 'about',msg='断言错误，判断URL失败')

    # @unittest.skip
    def test_003_document(self):

        try:
            self.click((By.CSS_SELECTOR, 'div.yuanjing-header3>div>div:nth-child(2)>div:nth-child(2)'))
            self.driver.implicitly_wait(2)
            about_title = self.driver.current_url
            self.assertEqual(about_title, self.base_url + '/document', msg='url断言错误')
        except Exception as e:
            print(e)

    def test_004_login(self):
        # 点击登录按钮进入到官网
        self.click((By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(3)'))
        # 校验登录页面的text
        ele = self.locate((By.CSS_SELECTOR,'div.page-section.center.third-login-wrapper > div > h2'))
        self.assertEqual(ele.text,'欢迎登录元境',msg='登录校验失败')

    def test_005_register(self):
        self.click((By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(4)'))
        current_url = self.driver.current_url
        self.assertEqual(current_url,'https://www.yuanjingio.com/account/register',msg='注册校验失败')



if __name__ == '__main__':
    suite = unittest.defaultTestLoader
    suite.discover('./','test*.py')
    dir_path = time.strftime('%Y-%m-%d_%H-%M-%S')
    timestr = time.strftime('%Y%m%d')
    # 生成的报告的名字和目录
    # filename = '../../Yuanjing_ui/test_report/' + timestr + '.html'
    #
    # fp = open(filename,'wb',encoding='utf-8')
    # runner = XTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     verbosity=1,
    #     title='Yuanjing',
    #     description='description....',
    #     language='en'
    # )  # 实例化runner
    # runner.run(suite)
    # fp.close()
    #
    filename = './report.html'
    with(open(filename,'wb',encoding='utf-8')) as f:

        runner = XTestRunner.HTMLTestRunner(
            stream=f,
            language='en'
        )
    runner.run(suite)