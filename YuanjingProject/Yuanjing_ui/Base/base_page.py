from selenium import webdriver
from time import time, sleep

from selenium.common.exceptions import NoSuchElementException
from Yuanjing_ui.Log import logger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class Keys(object):

    def __init__(self):
        self.driver = webdriver.Chrome()

        # 首先需要初始化一个chrome驱动


    #打开url
    def open(self,url):
        self.driver.maximize_window()
        sleep(1)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
        except:
            raise print('当前访问的URL：%s失败，请检查网络或者访问对象' %url)


    #定位元素  定位元素之后返回
    def locate(self,name):
        return self.driver.find_element(*name)


    # 对元素进行点击
    def click(self,name):
        self.locate(name).click()

    # 输入
    def input(self,value,txt):
        self.locate(value).clear()
        self.driver.implicitly_wait(2)
        self.locate(value).send_keys(txt)

    # 退出浏览器
    def quit(self):
        self.driver.quit()

    # 关闭浏览器标签页
    def close(self):
        self.driver.close()

    # 隐式等待
    def implicilty_wait(self,time):
        self.driver.implicitly_wait(time)

    # 定义显示等待
    def web_el_wait(self,value):
        return WebDriverWait(self.driver,10,0.5).until(lambda el: self.locate(*value),message='元素获取失败')

    # 切换窗口句柄
    def switch_frame(self,index):
        ele = self.driver.window_handles
        self.driver.switch_to_window(ele[index])

    # # 获取当前网页url
    # def get_current_url(self):
    #     url = self.get_current_url()
    #     return url

        # try:
        #     self.driver.switch_to.frame(*window_ele)
        #
        # except NoSuchElementException:
        #     try:
        #         self.driver.switch_to.frame(*window_ele)
        #     except:
        #         self.driver.switch_to.frame(self.locate(*window_ele))

    # 固定等待时间
    def sleep(self,time_):
        sleep(time_)

    # 定义悬停点击操作
    def suspension(self,value):
        ActionChains(self.driver).move_to_element(*value).perform()



#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
selenium基类
本文件存放了selenium基类的封装方法
"""


    #
    #
    #
    # def get_url(self, url):
    #     """打开网址并验证"""
    #     self.driver.maximize_window()
    #
    #
    #     try:
    #         self.driver.get(url)
    #         self.driver.implicitly_wait(10)
    #         log.info("打开网页：%s" % url)
    #     except TimeoutException:
    #         raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)
    #
    #
    # @staticmethod
    # def element_locator(func, locator):
    #     """元素定位器"""
    #     name, value = locator
    #     return func(cm.LOCATE_MODE[name], value)
    #
    # def find_element(self, locator):
    #     """寻找单个元素"""
    #     return WebPage.element_locator(lambda *args: self.wait.until(
    #         EC.presence_of_element_located(args)), locator)
    #
    # # def find_elements(self, locator):
    # #     """查找多个相同的元素"""
    # #     return WebPage.element_locator(lambda *args: self.wait.until(
    # #         EC.presence_of_all_elements_located(args)), locator)
    #
    # def elements_num(self, locator):
    #     """获取相同元素的个数"""
    #     number = len(self.find_elements(locator))
    #     log.info("相同元素：{}".format((locator, number)))
    #     return number
    # def input_text(self, locator, txt):
    #     """输入(输入前先清空)"""
    #     sleep(0.5)
    #     ele = self.find_element(locator)
    #     ele.clear()
    #     ele.send_keys(txt)
    #     log.info("输入文本：{}".format(txt))
    #
    # def is_click(self, locator):
    #     """点击"""
    #     self.find_element(locator).click()
    #     sleep()
    #     log.info("点击元素：{}".format(locator))
    #
    # def element_text(self, locator):
    #     """获取当前的text"""
    #     _text = self.find_element(locator).text
    #     log.info("获取文本：{}".format(_text))
    #     return _text
    #
    # @property
    # def get_source(self):
    #     """获取页面源代码"""
    #     return self.driver.page_source
    #
    # def refresh(self):
    #     """刷新页面F5"""
    #     self.driver.refresh()
    #     self.driver.implicitly_wait(30)
    #
    #








# # 封装的是公共方法
# import time
# from tools.get_logger import GetLogger
# import page
# from selenium.webdriver.support.wait import WebDriverWait
#
# log = GetLogger.get_logger()
#
#
# class Base:
#     # 0、初始化驱动（相当于Java中的构造函数,创建对象时，有参的初始化函数）
#     def __init__(self, driver):
#         # 操作之前执行日志记录操作步骤
#         log.info("[base]: 正在获取初始化driver对象:{}".format(driver))
#         self.driver = driver
#
#     # 1、查找元素的方法,返回元素对象
#     # 此处使用*loc作用，元组进行解包，python语法中有学习，传递元组进行元素定位解析
#     # def base_find_elements(seeout=30, plf, loc, timoll=0.5):
#     #     log.info("[base]: 正在定位:{} 元素，默认定位超时时间为: {}".format(loc, timeout))
#     #     # 使用显示等待获取元素
#     #     return WebDriverWait(self.driver,
#     #                          timeout=timeout,
#     #                          poll_frequency=poll).until(lambda x: x.find_element(*loc))
#
#
#     # 2、点击元素的方法(先定位元素，再调用点击方法)
#     def base_click_elements(self, loc):
#         log.info("[base]: 正在对:{} 元素实行点击事件".format(loc))
#         self.base_find_elements(*loc).click()
#
#         # element1 = driver.find_element_by_css_selector('.ush button')
#         # self.driver.execute_script("arguments[0].click();", self.base_find_elements(loc))
#
#     # 3、获取元素值的方法(先定位，再获取)
#     def base_get_value(self, loc):
#         log.info("[base]: 正在获取:{} 元素文本值".format(loc))
#         return self.base_find_elements(*loc).text
#
#     # 4、输入信息方法
#     def base_send_keys(self, loc, value):
#         # 定位元素
#         ele = self.base_find_elements(*loc)
#         # 先清除内容，记录操作日志
#         log.info("[base]: 正在对:{} 元素实行清空".format(loc))
#         ele.clear()
#         # 输入内容
#         log.info("[base]: 正在对:{} 元素输入内容为：{}".format(loc, value))
#         ele.send_keys(value)
#
#     # 5、截图方法
#     def base_get_image(self):
#         log.info("[base]: 断言出错，调用截图")
#         self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))
#
#     # 6、判断元素是否存在
#     def base_is_exits(self, loc):
#         try:
#             self.base_find_elements(loc,timeout=30)
#             log.info("[base]: {} 元素查找成功，存在页面".format(loc))
#             return True  # """代表存在"""
#         except Exception as e:
#             log.info("[base]: {} 元素查找失败，不存在当前页面".format(loc))
#             return False  # """代表不存在"""
#
#     # 7、回到首页面 方法
#     def base_index(self):
#         time.sleep(2)
#         log.info("[base]: 正在回到主页面")
#         self.driver.get(page.URL)
#
#     # 8、切换frame表单 方法
#     def base_switch_frame(self, name):
#         self.driver.switch_to.frame(name)
#
#     # 9、回到默认目录 方法
#     def base_default_content(self):
#         self.driver.switch_to.default_content()
#
#     # 10、切换窗口 方法 调用此方法  title>>>句柄>>>切换窗口
#     def base_switch_to_window(self, title):
#         # 日志
#         log.info("正在执行切换title值为：{}窗口 ".format(title))
#         self.driver.switch_to.window(self.base_get_title_handle(title))
#
#     # 11、获取指定title页面的handle方法
#     def base_get_title_handle(self, title):
#         # 获取当前页面所有的handles
#         for handle in self.driver.window_handles:
#             log.info("正在遍历handles：{}-->{}".format(handle, self.driver.window_handles))
#             # 切换 handle
#             self.driver.switch_to.window(handle)
#             log.info("切换 :{} 窗口".format(handle))
#             # 获取当前页面title 并判断 是否等于 指定参数title
#             log.info("判断当前页面title:{} 是否等于指定的title:{}".format(self.driver.title, title))
#             if self.driver.title == title:
#                 log.info("条件成立！ 返回当前handle{}".format(handle))
#                 # 返回 handle
#                 return handle
#
