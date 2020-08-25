import time

from selenium import webdriver

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
driver.quit()