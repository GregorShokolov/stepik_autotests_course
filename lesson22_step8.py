from selenium import webdriver
import time
import os
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(by='css selector', value='div.form-group input[name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(by='css selector', value='div.form-group input[name="lastname"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(by='css selector', value='div.form-group input[name="email"]')
    input3.send_keys("ivanpetrov@mail.ru")
    fileload = browser.find_element(by='id', value='file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    fileload.send_keys(file_path)
    button = browser.find_element(by='css selector', value='button.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()