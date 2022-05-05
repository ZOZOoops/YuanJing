from selenium import webdriver
import time

driver = webdriver.Chrome()
url  = "https://www.95505.com.cn/"
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.find_element_by_link_text("保险超市").click()
time.sleep(2)
h = driver.window_handles
driver.switch_to.window(h[-1])
driver.find_element_by_xpath("/html/body/div[3]/app-root/nz-layout/nz-content/app-home/nz-layout/nz-header/ul/li[5]/button").click()

