import datetime
import os.path
import time
from time import sleep
import unittest
from XTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from Yuanjing_ui.Base.base_page import Keys
class YuanJing(unittest.TestCase,Keys):

    # config = configparser.ConfigParser()  # 类的实例化
    # path = r'C:\Users\cc\PycharmProjects\Yuanjing_Project\Data\data.ini'
    # config.read(path)

    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.get('https://www.yuanjingio.com')
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.driver.close()


    def setUp(self):
        pass


    def teatDown(self):

        self.quit()


    # @unittest.skip()
    def test_001_login(self):
        # self.url = 'https://www.yuanjingio.com/'
        # self.driver.implicitly_wait(5)
        # self.open(self.url)
        # self.driver.maximize_window()
        # sleep(2)
        # self.assertEqual(self.driver.current_url, "https://www.yuanjingio.com/", msg="你的结果校验错误")
        # # 两句重复的代码
        # # try:
        # #     self.assertEqual(self.driver.current_url, 'https://www.yuanjingio.com/')
        # # except:
        # #     print('结果校验错误')
        self.open(url='https://www.yuanjingio.com')
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.click((By.CLASS_NAME,'login'))
        self.driver.implicitly_wait(2)
        self.input((By.NAME,'domainAccount'),'13132221817')
        self.driver.implicitly_wait(2)
        self.input((By.NAME,'password'),'Liu123123')
        sleep(2)
        title = self.driver.title
        self.assertEqual(title,'统一登录中心',msg='网页标题验证错误')
        self.click((By.CLASS_NAME,'sso-btn-submit'))
        self.driver.implicitly_wait(2)
        # jiaoyan = self.driver.find_element(By.CLASS_NAME,'tenantselect-checkLogin')
        #
        # self.assertEqual(self.driver.find_element(By.CLASS_NAME,'tenantselect-checkLogin'),'您可以选择以下企业登录',msg='校验选择企业登录失败')
        self.click((By.XPATH,'//*[@id="App"]/div/div/div[3]/div/button[2]/span'))
        self.driver.implicitly_wait(3)
        self.click((By.XPATH,'//*[@id="App"]/div/div/div[2]/div/div[3]/div'))
        self.driver.implicitly_wait(2)
        self.click((By.CLASS_NAME,'kuma-button kuma-button-primary'))
        sleep(5)
        # jiaoyan1 = self.driver.find_element(By.)
            #       提交按钮


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()

    suite = unittest.defaultTestLoader.discover(pattern='./test*.py')
    # suite.addTest('test_001_login')
    dir_path = time.strftime('%Y-%m-%d_%H-%M-%S')
    file_name = '../test_report/' + dir_path + '_test_result.html'
    with open(file_name,'wb') as f:
        runner = HTMLTestRunner(
            stream= f,
            verbosity=1,
            title='Yuanjing',
            description='description....',
            language='en'
        )  # 实例化runner
    runner.run(suite)
    # test_dir = './'
    # discover = unittest.defaultTestLoader.discover(test_dir,'test*.py')
    # # runner.run(suite)
    # runner.run(discover)
    # report_title = '测试报告'
    # report_file = './HTMLreport.html'
    # with open(report_file,'wb') as f:
    #     runner = HTMLTestRunner(steam = report_file,title=report_title)
    #     runner.run(discover)


