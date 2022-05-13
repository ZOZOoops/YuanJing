from selenium import webdriver


class Browser():

    '''
    打开浏览器函数
    当前驱动只存在三种
    '''
    def startBrowser(self,name):

        try:

            if name == 'chrome' or 'Chrome':
                print('启动Chrome浏览器')
                driver = webdriver.Chrome()
                return driver

            elif name == 'Firefox' or 'firefox' or 'ff':
                print('启动Firefox浏览器')
                driver = webdriver.Firefox()
                return driver
            elif name == 'Edge' or 'edge':
                print('启动Edge浏览器')
                driver = webdriver.Edge()
                return driver
            else:
                print('no found this browser,you can use "chrome" or "firefox" or "edge"')
        except Exception as msg:
            print('启动{}浏览器出现异常:{}'.format(name,msg))


