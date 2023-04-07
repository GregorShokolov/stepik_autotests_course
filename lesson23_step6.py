from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.CLASS_NAME, 'trollface.btn')
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_num = browser.find_element(By.ID, 'input_value')
    x = x_num.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')
    button2.click()

finally:
    time.sleep(10)
    browser.quit()
