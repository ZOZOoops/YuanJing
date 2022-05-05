import configparser
import logging
import os
import unittest
import time
import XTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from Yuanjing_ui.Base.base_page import Keys
from configparser import ConfigParser

class Yuanjing_alreadylogin_view(unittest.TestCase,Keys):

    conf = configparser.ConfigParser
    # conf.read('./Config/data.ini')
    base_url = 'https://www.yuanjingio.com/index'
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.open(self.base_url)
        # self.click((By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(3)'))

        self.input((By.NAME,'domainAccount'),'13132221817')
        self.implicilty_wait(2)
        self.input((By.NAME,'password'),'Liu123123')
        self.click((By.CLASS_NAME,'sso-btn-submit'))
        self.sleep(2)
        # 选择团队进行登录
        self.click((By.CSS_SELECTOR,'div.page-tenantselect-section-publicAccount > div > div:nth-child(3)'))
        self.click((By.CSS_SELECTOR,'div.tenantselect-btns > button:nth-child(2)'))
        self.sleep(5)
    def tearDown(self) -> None:
        self.quit()

    def test_001_console(self):
        # 点击控制台下拉窗
        self.click((By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(3)'))
        self.sleep(3)
        # 进入开发者控制台
        self.click((By.CSS_SELECTOR,'div.next-overlay-inner > div > div:nth-child(2)'))
        self.sleep(3)
        # 保持当前窗口处于最新
        try:
            self.switch_frame(-1)
        except:
            raise '切换frame异常'
        current_url = self.driver.current_url
        self.assertEqual(current_url,'https://www.yuanjingio.com/console',msg='控制台url断言失败')

    # @unittest.skip
    def test_002_personal_msg(self):
        # 显示等待元素是否出现
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located
                                                ((By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(4)')))
        # 点击个人头像
        self.click((By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(4)'))

        # 进入到消息中心
        self.click((By.CSS_SELECTOR,'div.next-overlay-inner > div:nth-child(2) > div:nth-child(1)'))
        # 获取当前url并进行校验是否与预期相等
        self.sleep(2)
        url = self.driver.current_url
        self.assertEqual(url,'https://www.yuanjingio.com/notification',msg='消息中心url校验错误')

    def test_003_personal_team(self):
        pass

    def test_004_personal_center(self):
        pass

if __name__ == '__main__':
    suite = unittest.defaultTestLoader
    suite.discover('./*test.py')
    dir_path = time.strftime('%Y-%m-%d_%H-%M-%S')
    timestr = time.strftime('%Y%m%d', time.localtime(time.time()))
    # 生成的报告的名字和目录
    filename = '../test_report/' + timestr + ".html"
    with open(filename,'wb') as f:
        runner = XTestRunner.HTMLTestRunner(
            verbosity=1,
            stream=f,
            title='yuanjing',
            description='元境测试报告',
            language='en'
        )
        runner.run(suite)


