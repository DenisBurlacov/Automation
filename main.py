# 1.Open browser
# 2. Go to web page
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(5)
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(5)