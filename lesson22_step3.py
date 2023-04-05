from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a_num = browser.find_element(by='id', value='num1')
    a = a_num.text
    b_num = browser.find_element(by='id', value='num2')
    b = b_num.text
    y = int(a) + int(b)
    select = Select(browser.find_element(by='tag name', value='select'))
    select.select_by_value(str(y))
    button = browser.find_element(by='css selector', value='button.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()