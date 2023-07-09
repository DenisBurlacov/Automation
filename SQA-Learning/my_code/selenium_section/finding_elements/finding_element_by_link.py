from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('http://mystore.local')

cart_element = driver.find_element(By.LINK_TEXT, "Cart")
print(cart_element.text)
acct_element = driver.find_element(By.LINK_TEXT, 'My account')
print(acct_element.text)

acct_element_p = driver.find_element(By.PARTIAL_LINK_TEXT, 'account')
print(acct_element_p.text)

futter_link_partial = driver.find_element(By.PARTIAL_LINK_TEXT, 'Built with Storefront')
print(futter_link_partial.text)

# driver.find_element(By.LINK_TEXT, 'O items')
