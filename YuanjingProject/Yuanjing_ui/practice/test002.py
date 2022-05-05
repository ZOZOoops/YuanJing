
import configparser
from time import sleep
from configparser import ConfigParser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Yuanjing_ui.Base.base_page import Keys



class PageObject(Keys):

    base_url = 'https://www.yuanjingio.com/'
    data_path = r'../Config/data.ini'
    conf = configparser.ConfigParser()
    conf.read(data_path)
    # 通过列表的方法读取

    def yuanjing_login(self):
        self.open(self.base_url)
        self.driver.maximize_window()
        sleep(2)
        self.click((By.CLASS_NAME,'login'))
        self.driver.implicitly_wait(3)
        self.input((By.NAME,'domainAccount'),'13132221817')
        self.driver.implicitly_wait(2)
        self.input((By.NAME,'password'),'Liu123123')
        self.click((By.CLASS_NAME,'sso-btn-submit'))
        self.click((By.CSS_SELECTOR,'div.page-tenantselect-section-publicAccount-items>div:nth-of-type(3)'))
        self.driver.implicitly_wait(2)

        try:
            self.click((By.CLASS_NAME,'kuma-button kuma-button-primary'))
        except Exception as e:
            raise e

        finally:
            self.close()
if __name__ == '__main__':
    login = PageObject()
    login.yuanjing_login()














