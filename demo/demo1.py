#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver=webdriver.Chrome(executable_path="D:/APP/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.yuanrenxue.com")
try:
    element=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"search-show"))
    )
    element.click()
except Exception:
    print('not locate search-show')
    driver.quit()
else:
    search=driver.find_element_by_class_name('search-input')
    search.send_keys(u'python教程')
    time.sleep(5)
    search.send_keys(Keys.RETURN)
    time.sleep(5)
    element=driver.find_element_by_tag_name('body')
    element.send_keys(Keys.DOWN)
    element.send_keys(Keys.DOWN)
    time.sleep(5)
    driver.quit()

time.sleep(60)
cookies=driver.get_cookies()
with open("D:/python files/demo/Scripts/wb_cookies","wb") as f:
    pickle.dump(cookies,f)
print('done')
driver.quit()