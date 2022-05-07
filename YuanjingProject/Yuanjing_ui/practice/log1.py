from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
d = webdriver.Chrome()
d.get('https://www.yuanjingio.com')
d.maximize_window()
sleep(2)
ele = d.find_element(By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div.next-box > div > div > div')
ActionChains(driver=d).move_to_element(ele).perform()
