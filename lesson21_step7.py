from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_chest = browser.find_element(by='id', value='treasure')
    x = x_chest.get_attribute('valuex')


    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    input1 = browser.find_element(by='id', value='answer')
    input1.send_keys(y)
    option1 = browser.find_element(by='id', value='robotCheckbox')
    option1.click()
    option2 = browser.find_element(by='id', value='robotsRule')
    option2.click()
    button = browser.find_element(by='css selector', value='button.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()