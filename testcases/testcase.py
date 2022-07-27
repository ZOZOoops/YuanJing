import unittest
from time import sleep

from common.common_basepage import Base_Keys
from common.common_elements import login_elements
from configparser import ConfigParser




class TestCase(unittest.TestCase,Base_Keys,login_elements):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        self.quit()


    # 登录成功case
    def test_001_login_success(self):
        username = 'zidonghua'
        pwd = 'Liu123123'
        url = 'https://www.yuanjingio.com/index'
        Base_Keys('chrome')
        self.open(url)
        self.input(self.name_input,username)
        self.input(self.password_input,pwd)
        sleep(2)
        self.assertEqual('','',msg='')

    # 登录失败case
    def test_002_right_account(self):
        username = ''
        pwd = ''
        url = 'https://www.yuanjingio.com/index'

        self.open(url)
        self.input(self.name_input, username)
        self.input(self.password_input, pwd)
        self.assertEqual('', '', msg='')

    def test_003_login(self):
        pass

    def test_004_logout(self):
        pass

    def test_005_about(self):
        pass

    def test_006_document(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestSuite()

