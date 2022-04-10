import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True) # Avoiding browser for closing after opened
opt.add_argument('--ignore-certificate-errors') # Handle node connection error (0x1F)
opt.add_argument("--disable-webgl")
opt.add_argument("--disable-notifications") # Disable browser push notification
opt.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
driver.implicitly_wait(30)
driver.get('https://www.oyorooms.com/id/hotels-in-yogyakarta/')
driver.maximize_window()

# Get url for all pages (href attributes)
page_url = [url.get_attribute('href') for url in driver.find_elements(By.CLASS_NAME, 'ListingPagination__pageContainer--page')]

for page in page_url:
    driver.get(page)

driver.close()
driver.quit()

