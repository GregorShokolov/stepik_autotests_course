from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_num = browser.find_element(by='id', value='input_value')
    x = x_num.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    input1 = browser.find_element(by='id', value='answer')
    input1.send_keys(y)
    option1 = browser.find_element(by='id', value='robotCheckbox')
    option1.click()
    option2 = browser.find_element(by='id', value='robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    button = browser.find_element(by='css selector', value='button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()
