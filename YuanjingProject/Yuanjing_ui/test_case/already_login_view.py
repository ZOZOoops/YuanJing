import configparser
import unittest
from datetime import time

from XTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from Yuanjing_ui.Base.base_page import Base_Keys
from Yuanjing_ui.Log import logger
from Yuanjing_ui.Log.logger import Logger
from Yuanjing_ui.utils.logger import log
from selenium.webdriver.common.action_chains import ActionChains


class Yuanjing_alreadylogin_view(unittest.TestCase,Base_Keys,Logger):

    conf = configparser.ConfigParser
    filename = '../Config/data.ini'
    # config.read(filename)
    testproj_name = '元境测试项目testing'

    base_url = 'https://www.yuanjingio.com/index'

    def setUp(self):
        # option = webdriver.ChromeOptions()
        # option.add_argument('window-size=1920x1080')
        # self.driver = webdriver.Chrome()
        self.driver = self.chooseBrowser('edge') # 此处选定输入浏览器的版本
        self.open(self.base_url)
        # self.click((By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(3)'))
        self.input((By.NAME,'domainAccount'),'13132221817')
        self.implicilty_wait(2)
        self.input((By.NAME,'password'),'Liu123123')
        self.click((By.CLASS_NAME,'sso-btn-submit'))
        self.sleep(2)
        # 选择团队进行登录
        self.click(
            (By.CSS_SELECTOR, 'div.page-tenantselect-section-publicAccount > div > div:nth-child(3)'))  # 选择第三个团队登录
        # 点击确认登录按钮
        self.click((By.CSS_SELECTOR, 'div.tenantselect-btns > button:nth-child(2)'))
        self.sleep(5)

    def tearDown(self) -> None:
        self.quit()

    # @unittest.skip
    def test_001_console(self): # 进入到控制台项目管理

        # 点击控制台下拉窗
        self.click((By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(3)'))
        self.sleep(2)
        # 进入开发者控制台
        self.click((By.CSS_SELECTOR,'div.next-overlay-inner > div > div:nth-child(2)'))
        self.sleep(2)
        # 保持当前窗口处于最新
        self.switch_window(-1)
        current_url = self.driver.current_url
        print('当前标签页URL为：{}'.format(self.driver.current_url))
        self.implicilty_wait(2)
        try: # 点击创建项目按钮
            self.click((By.CSS_SELECTOR,'div.main-wrapper > div > div > div > div > div > div > button'))
        except Exception as e:
            print('An Exception has haapend: {}'.format(e))
        self.implicilty_wait(2)
        # 输入创建项目的名称
        self.input((By.ID,'gameName'),self.testproj_name)
        self.sleep(2)
        # 点击确认按钮创建项目
        self.click((By.CSS_SELECTOR,'div.next-dialog-body > form > div:nth-child(3) > button:nth-child(2)'))
        # 在此进行判断,当前创建的项目是否重复，如果重复，找到重名的项目删除
        # if self.locate((By.CSS_SELECTOR,'body > div: nth - child(10) > div > div')).text == '项目名称已经存在，请重新命名!':
        #     log.error('创建项目名称重复')
        #     # self.locate((By.CSS_SELECTOR,'')).
        #     pass
        self.sleep(2)
        # 创建项目的名称
        proj_name = self.locate((By.CSS_SELECTOR,'div.next-loading-wrap > div > div > div:nth-child(1) > div > div > div > div:nth-child(1)')).text
        log.info(proj_name) # 打印当前创建项目的名称
        #  校验创建项目是否成功，使用项目名称进行校验
        self.assertEqual(self.testproj_name,proj_name,msg='创建项目失败')
        self.sleep(2)
        ele = self.driver.find_element(By.CSS_SELECTOR,'div.next-loading-wrap > div > div > div:nth-child(1)')
        ActionChains(self.driver).move_to_element(ele).perform()
        self.sleep(2)
        # 悬浮编辑按钮
        del_ele = (By.CSS_SELECTOR,'#ice-container > section > section > section > div > div > div > div > div > div > div > div > '
                                   'div.next-loading.next-loading-inline > div > div.Console--consoleContent--R35ex4l > div > div:nth-child(1) > div > div:nth-child(2) > div > div')
        del_btn = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located(del_ele))
        del_btn.click()
        self.sleep(2)
        # 点击删除按钮
        self.click((By.CSS_SELECTOR,'div.next-overlay-wrapper > ul > li:nth-child(2) > div'))
        self.sleep(2)
        # 删除点击确认
        self.click((By.CSS_SELECTOR,'div.next-overlay-wrapper > div > div:nth-child(2) > button:nth-child(1)'))

        self.sleep(2)
        ele = self.locate((By.CSS_SELECTOR,'body > div.next-overlay-wrapper.opened > div'))
        self.assertEqual('项目删除成功',ele.text,msg='校验项目删除失败')
        print('进入控制台项目管理用例测试通过')

    # @unittest.skip
    def test_002_personal_msg(self): # 验证进入消息中心
        # 显示等待元素是否出现
        try:
            WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located
                                                ((By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(4)')))
        except :
            raise '个人头像打开失败'
        # 点击个人头像
        self.click((By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(4)'))

        # 进入到消息中心
        self.click((By.CSS_SELECTOR,'div.next-overlay-inner > div:nth-child(2) > div:nth-child(1)'))
        # 获取当前url并进行校验是否与预期相等
        self.sleep(2)
        window_handle = self.driver.window_handles
        self.sleep(2)
        self.driver.switch_to.window(window_handle[-1])
        self.sleep(2)
        url = self.driver.current_url
        self.assertEqual(url,'https://www.yuanjingio.com/notification',msg='消息中心url校验错误') # 判断是否进入到消息中心
        print('消息中心用例测试通过')

    # @unittest.skip
    def test_003_personal_team(self): # 验证进入团队管理
        # 点击个人头像
        self.click((By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(4)'))
        self.sleep(2)
        # 进入到团队管理
        self.click((By.CSS_SELECTOR,'div.next-overlay-inner > div:nth-child(2) > div:nth-child(3)'))
        # 获取当前所有窗口并且切换窗口到最新
        window_handle = self.driver.window_handles
        self.sleep(2)
        self.driver.switch_to.window(window_handle[-1])
        url = self.driver.current_url
        self.assertEqual(url,'https://www.yuanjingio.com/account/ram/users',msg='判断团队管理url错误')  # 判断当前标签页url是否与预期中相等
        print('团队管理首页用例测试通过')
    # @unittest.skip

    def test_004_personal_center(self): # 个人中心
        # 点击个人头像
        self.click((By.CSS_SELECTOR, 'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(4)'))
        self.sleep(2)
        # 进入个人中心
        self.click((By.CSS_SELECTOR, 'div.next-overlay-inner > div:nth-child(2) > div:nth-child(2)'))
        # 获取当前所有窗口并且切换窗口到最新
        window_handle = self.driver.window_handles
        self.sleep(2)
        self.driver.switch_to.window(window_handle[-1])
        url = self.get_current_url()
        self.assertEqual('https://www.yuanjingio.com/account/user/info',url, msg='判断个人中心url错误')  # 判断当前标签页url是否与预期中相等
        print('个人中心用例测试通过')
        log.error('个人中心用例测试通过')




if __name__ == '__main__':

    discover = unittest.defaultTestLoader.discover('../TestCase/', 'test*.py')
    file_dir = '../test_log/'
    time_fmt = ('%Y-%m-%d_%H-%M-%S')
    file_name = file_dir + time.strftime(time_fmt) + 'report.html'
    with open(file_name,'a') as f:
        runner = HTMLTestRunner(
            stream=f,
            verbosity=1,
            title='Yuanjing',
            description='元境用例测试',
            language='zh-CN'
        )

    runner.run(discover)









