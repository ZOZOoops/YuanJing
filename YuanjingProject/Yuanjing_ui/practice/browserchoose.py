# coding:utf-8
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from Yuanjing_ui.Log.logger import Logger

def startBrowser(name):
    """
    打开浏览器函数，"firefox"、"chrome"、"ie"、"edge"
    """
    try:
        if name == 'Firefox' or name == 'firefox' or name == 'ff':
            print('启动Firefox浏览器')
            driver = webdriver.Firefox()
            return driver

        elif name == 'chrome' or name ==  'Chrome' or name ==  'CHROME':
            print('启动Chrome浏览器')
            driver = webdriver.Chrome()
            return driver

        elif name == 'Edge' or name ==  'edge' or name ==  'EDGE':
            print('启动Edge浏览器')
            driver = webdriver.Edge()
            return driver

        elif name == 'IE' or name ==  'ie' or name ==  'Ie':
            print('启动IE浏览器')
            driver = webdriver.Ie()
            return driver

        else:
            print('no found this browser,you can use "chrome" or "firefox" or "edge"')

    except Exception as msg:
        print('启动{}浏览器出现异常:{}'.format(name, msg))


def login(name):
    print('==login==')
    driver = startBrowser(name)
    driver.get('https://www.yuanjingio.com/index')
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.NAME,'domainAccount').send_keys('13132221817')
    time.sleep(2)
    driver.find_element(By.NAME,'password').send_keys('Liu123123')
    driver.implicitly_wait(2)
    driver.find_element(By.CLASS_NAME,'sso-btn-submit').click()
    time.sleep(2)
    # 选择团队进行登录
    driver.find_element(By.CSS_SELECTOR,'div.page-tenantselect-section-publicAccount > div > div:nth-child(3)').click()
    driver.implicitly_wait(2)
    # 点击登录
    driver.find_element(By.CSS_SELECTOR,'div.tenantselect-btns > button:nth-child(2)').click()
    time.sleep(2)
    print('====完成登录测试====')
    driver.quit()

def open_portal(name): # 打开元境官网
    base_url = 'https://www.yuanjingio.com'
    d = startBrowser(name)
    d.get(base_url)
    d.maximize_window()
    time.sleep(3)

def no_login_view(name):
    print('==正在开始未登录浏览测试==')
    base_url = 'https://www.yuanjingio.com'
    d = startBrowser(name)
    d.get(base_url)
    d.maximize_window()
    time.sleep(3)
    current_url = d.current_url
    # 校验官网的URL是否相等
    try:
        assert current_url == 'https://www.yuanjingio.com/'
    except:
        raise '断言校验失败，url与预期结果：{}不相等' .format(base_url)
    d.quit()
    # 进入到关于我们 about
def about(name):
    print('进入到关于我们')
    base_url = 'https://www.yuanjingio.com'
    d = startBrowser(name)
    d.get(base_url)
    d.maximize_window()
    time.sleep(3)
    # 点击关于我们
    d.find_element(By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(1)').click()
    d.implicitly_wait(2)

    window_handles = d.window_handles
    # 切换到最新的窗口验证url是否正确
    d.switch_to.window(window_handles[-1])
    d.implicitly_wait(2)
    ele = d.current_url
    print(ele)
    try:
        assert ele == base_url + '/about'
    except :
        raise AssertionError

    print('====完成测试====')
    d.quit()

def document(name):

    print('==document==')
    base_url = 'https://www.yuanjingio.com'
    d = startBrowser(name)
    d.get(base_url)
    d.maximize_window()
    time.sleep(2)
    # 点击文档
    d.find_element(By.CSS_SELECTOR, 'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(2)').click()
    time.sleep(2)
    window_handles = d.window_handles
    # 切换到最新的窗口验证url是否正确
    d.switch_to.window(window_handles[-1])
    d.implicitly_wait(2)
    ele = d.current_url
    print(ele)

    try:
        assert ele == base_url + '/document'
    except :
        raise AssertionError



    print('====完成测试====')
    d.quit()


# 函数里面需要传一个浏览器参数

if __name__ == "__main__":
    names = ["chrome", "firefox", "edge"]
    for name in names:
        login(name)
        no_login_view(name)
        about(name)
        document(name)
    print('='*10 ,'全部进程结束','='*10 )
