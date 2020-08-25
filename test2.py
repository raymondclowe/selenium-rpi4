from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless') 
options.add_argument('--no-sandbox')

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=options)  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(3) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(3) # Let the user actually see something!
print(driver.title)
driver.quit()