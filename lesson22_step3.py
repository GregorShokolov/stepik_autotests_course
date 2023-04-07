from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a_num = browser.find_element(By.ID, 'num1')
    a = a_num.text
    b_num = browser.find_element(By.ID, 'num2')
    b = b_num.text
    y = int(a) + int(b)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(y))
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
