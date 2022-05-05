from time import sleep

from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.get('https://www.yuanjingio.com')
sleep(3)
d.maximize_window()
d.find_element_by_css_selector('div.needLogin > div:nth-of-type(1) ').click()
d.implicitly_wait(2)
d.find_element(By.NAME,'domainAccount').send_keys('13132221817')
d.implicitly_wait(2)
d.find_element(By.NAME,'password').send_keys('Liu123123')
d.implicitly_wait(2)
d.find_element(By.CLASS_NAME,'sso-btn-submit').click()
d.implicitly_wait(2)
ele = d.find_element(By.CLASS_NAME,'tenantselect-checkLogin')
print(ele.text)
try:
    assert ele.text == '您可以选择以下企业登录'
except :
    raise ('断言错误')
d.find_element(By.CSS_SELECTOR,'div.page-tenantselect-section-publicAccount > div > div:nth-of-type(3)').click()

try:
    # d.find_element(By.CSS_SELECTOR,'#App > div > div > div.page-tenantselect-section-btns >'
    #                                ' div > button.kuma-button.kuma-button-primary').click()
    d.find_element(By.CSS_SELECTOR, 'div .page-tenantselect-section-btns > div > button:nth-of-type(2)').click()

except:
    d.close()
sleep(3)
ele = d.find_element(By.CSS_SELECTOR,'span.next-badge')
ActionChains(d).move_to_element(ele).perform()    # 此处悬浮需要一直hover
sleep(5)

d.find_element(By.CSS_SELECTOR,'div.next-overlay-wrapper div div:nth-of-type(2) div:nth-of-type(2)').click() # 进入个人中心
sleep(5)
# 当前不能选择点击个人中心，导致不能进入到个人中心


