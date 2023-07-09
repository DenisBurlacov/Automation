from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('file:///Users/den/PycharmProjects/Automation/SQA-Learning/my_code/selenium_section/waits/page_with_slow_image.html')
time.sleep(4)