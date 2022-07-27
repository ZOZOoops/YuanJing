# -*-coding:utf-8-*-

from time import time, sleep
from common_choosebrowser import choose_browser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Base_Keys(object):   # 使用调用Base_keys类的时候，需要输入浏览器的名称选择浏览器进行启动

    def __init__(self,name):
        """
        初始化浏览器启动
        """
        self.driver = choose_browser(name)
    """
        首先需要初始化一个chrome驱动
        当前只支持：Chrome 、 Firefox 、Edge 、Opera

    """

    #打开url
    def open(self,url):

        self.driver.maximize_window() # 最大化窗口
        sleep(2)

        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
        except:
            raise print(f'当前访问的URL：{url}失败，请检查网络或者访问对象')


    # 定位元素
    def locate(self,name):
        '''

        :param name:定位的元素名称
        :return:  返回元素名称
        name: (By.method,'元素名称')  用*name可变长元组进行解析
        '''
        return self.driver.find_element(*name)


    # 对元素进行点击
    def click(self,name):
        '''

        :param name: (By.method,'元素名称')  用*name可变长元组进行解析
        :return:
        调用locate方法 然后将其返回的内容做点击操作
        '''
        self.locate(name).click()

    # 输入
    def input(self,value,txt):
        '''

        :param value: (By.method,'元素名称')  用*value可变长元组进行解析
        :param txt: 输入的文本
        :return:
        '''
        self.driver.find_element(*value).clear() # 首先清空输入框文本
        self.driver.implicitly_wait(2)
        self.driver.find_element(*value).send_keys(txt) # 再进行文本的输入

    # 退出浏览器
    def quit(self):
        self.driver.quit()

    # 关闭浏览器标签页
    def close(self):
        self.driver.close()

    # 隐式等待
    def implicilty_wait(self,time):
        '''

        :param time: seconds
        :return:
        '''
        self.driver.implicitly_wait(time)

    # 定义显示等待
    def web_el_wait(self,value):

        '''
        :param value:
        value格式 (By.name,'kw')
        WebDriverWait(self.driver,10,0.5) 最大等待时间10s，每0.5秒进行一次查询元素
        :return:
        '''
        return WebDriverWait(self.driver,10,0.5).until(lambda el: self.locate(value),message='元素获取失败')

    # 切换窗口句柄
    def switch_window(self,index):
        """

        :param index: 索引值，索引值为-1表示当前标签页最新的窗口  从左往右：0开始
        :return:
        """
        ele = self.driver.window_handles # 得到当前窗口所有的句柄
        self.driver.switch_to.window(ele[index])  # 通过索引切换当前的窗口标签位置


    # 固定等待时间
    def sleep(self,time_):
        sleep(time_)


    # 定义悬停点击操作
    def suspension(self,value):
        location = self.locate(value)
        ActionChains(self.driver).move_to_element(location).perform()




    # 切换frame表单
    def switch_frame(self, name):
        self.driver.switch_to.frame(self.locate(name))


    # 9、切换iframe框之后，回到默认内容框
    def back_default_content(self):
        self.driver.switch_to.default_content()


    # 获取当前网页URL
    def get_current_url(self):
        return self.driver.current_url

    # 获取当前网页title
    def get_current_tile(self):
        return self.driver.title

    # Keys操作 点击鼠标右键
    def context_click(self,value):
        ActionChains.context_click(self.locate(*value))

    # 通过js定位点击元素
    def js_click(self,name):
        self.driver.execute_script('arguments[0].click()',self.locate(name))
