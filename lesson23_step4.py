from selenium import webdriver
import time
import math
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(by='class name', value='btn.btn-primary')
    button1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_num = browser.find_element(by='id', value='input_value')
    x = x_num.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    input1 = browser.find_element(by='id', value='answer')
    input1.send_keys(y)
    button2 = browser.find_element(by='css selector', value='button.btn-primary')
    button2.click()
finally:
    time.sleep(10)
    browser.quit()