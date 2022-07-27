from selenium import webdriver

def choose_browser(name):
    # 输入浏览器的名称，生成不同的webdriver对象
    if name == 'chrome' or name == 'Chrome':
        try:
            driver = webdriver.Chrome()
            return driver
        except:
            raise Exception('初始化当前浏览器:{}失败'.format(name))

    if name == 'firefox' or name == 'Firefox' or name == 'ff':
        try:
            driver = webdriver.Chrome(executable_path='../webdrivers/geckodriver.exe')
            return driver
        except:
            raise Exception('初始化当前浏览器:{}失败'.format(name))

    if name == 'edge' or name == 'Edge':
        try:
            driver = webdriver.Edge(executable_path='../webdrivers/msedgedriver.exe')
            return driver
        except:
            raise Exception('初始化当前浏览器:{}失败'.format(name))

    if name == 'opera' or name == 'Opera':
        try:
            driver = webdriver.Opera(executable_path='../webdrivers/operadriver.exe')
            return driver
        except:
            raise Exception('初始化当前浏览器：{}失败'.format(name))

    else:
        print("当前只支持：Chrome 、 Firefox 、Edge 、Opera", '允许输入的浏览器名称为：chrome、Chrome')