from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from Yuanjing_ui.Base.base_page import Keys
# "登录账号输入框" = name,'domainAccount'
# "登录密码输入框" = name,'password'
# "登录按钮" = classname,'sso-btn-submit'
# "选择团队" = css selector,'div.page-tenantselect-section-publicAccount > div > div:nth-child(1)' 括号输入的数字代表当前团队在列表中的索引，可以通过索引值选定需要登录的团队
# "选择团队之后提交按钮" = css selector,'div.tenantselect-btns > button:nth-child(2)'
# "选择团队之后上一步按钮" = css selector,'div.tenantselect-btns > button:nth-child(1)'
# “注册” = css selector，‘div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(4)’
d = webdriver.Chrome()

d.get('https://www.yuanjingio.com')
d.maximize_window()
sleep(3)

d.find_element(By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(3)').click()
d.implicitly_wait(2)
# 输入账号
d.find_element(By.NAME,'domainAccount').send_keys('13132221817')
# k.input((By.NAME,'domainAccount'),'13132221817')
# k.input((By.NAME,'password'),'Liu123123')
d.implicitly_wait(2)
# 输入密码
d.find_element(By.NAME,'password').send_keys('Liu123123')
# k.click((By.CLASS_NAME,'sso-btn-submit'))
# 点击登录
d.find_element(By.CLASS_NAME,'sso-btn-submit').click()
d.implicitly_wait(2)
# k.click((By.CSS_SELECTOR,'div.page-tenantselect-section-publicAccount > div > div:nth-child(1)'))
# 选择第一个团队进行登录
d.find_element(By.CSS_SELECTOR,'div.page-tenantselect-section-publicAccount > div > div:nth-child(3)').click()
# k.click((By.CSS_SELECTOR,'div.tenantselect-btns > button:nth-child(2)'))
d.implicitly_wait(2)
# 点击提交
d.find_element(By.CSS_SELECTOR,'div.tenantselect-btns > button:nth-child(2)').click()
# # 进入到首页点击个人头像
# d.find_element(By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(4)').click()
# d.implicitly_wait(2)
# # 进入到消息中心
# d.find_element(By.CSS_SELECTOR,'div.next-overlay-inner > div:nth-child(2) > div:nth-child(1)').click()
# # 切换到第一个窗口
# d.switch_to_window(handle)
# d.implicitly_wait(2)
sleep(3)
# 点击控制台
d.find_element(By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(3)').click()
d.implicitly_wait(2)
# 点击开发者控制台
d.find_element(By.CSS_SELECTOR,'div.next-overlay-inner > div > div:nth-child(2)').click()
sleep(2)
# 切换到第二个窗口
try:
    handle = d.window_handles[-1]
    d.switch_to.window(handle)
except:
    raise '切换窗口异常'
d.implicitly_wait(2)
sleep(2)
# 点击新建项目
d.find_element(By.CSS_SELECTOR,'div.main-wrapper > div > div > div > div > div > div.next-box.Console--searchWrapper--QYmD4IT > button').click()


sleep(5)
# close 是关闭当前浏览器标签页
d.quit()