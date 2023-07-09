from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://mystore.local/')

product = driver.find_element(By.CLASS_NAME, 'product')
products = driver.find_elements(By.CLASS_NAME, 'product')
# print(product)
# print('++++++++++++++++++++++++')
# print(products)

# order_by = driver.find_element(By.NAME, 'orderby')
# print(order_by.text)

all_links = driver.find_elements(By.TAG_NAME, 'a')
print(f'Found number of "a"  tag: {len(all_links)}')
time.sleep(4)