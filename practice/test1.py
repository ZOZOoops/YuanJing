from common.common_basepage import Base_Keys


class testcase(Base_Keys):

    def openurl(self):
        self.open('https://www.yuanjingio.com')


a = testcase('chrome')
a.openurl()