from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://mystore.local/')

card = driver.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-7 > a')
card.click()
time.sleep(7)
driver.quit()

