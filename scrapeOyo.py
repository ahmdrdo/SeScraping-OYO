from unicodedata import category
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

# Get url for all hotels
hotel_url = []
for page in page_url:
    driver.get(page)
    hotel_url.extend(url.get_attribute('href') for url in driver.find_elements(By.CSS_SELECTOR, 'a.c-nn640c'))

hotel_name = []
location = []
rate = []
facility = []
category = []
# Scrape hotel info, page by page
for hotel in hotel_url:
    driver.get(hotel)
    time.sleep(2) # Expect delay on loading page
    hotel_name.append(driver.find_element(By.CSS_SELECTOR, 'h1.c-1wj1luj').text)
    location.append(driver.find_element(By.CSS_SELECTOR, '[itemprop="streetAddress"]').text)
    rate.append(float(driver.find_element(By.CSS_SELECTOR, 'span.c-1uxth7l').text))
    facility.append(', '.join([i.text for i in driver.find_elements(By.CSS_SELECTOR, 'div.c-12w6zty')]))
    category.append(', '.join([i.text for i in driver.find_elements(By.CSS_SELECTOR, 'span.c-2j9z2q')]))

hotel_df = pd.DataFrame({
    'hotel_name': hotel_name,
    'location': location,
    'rate': rate,
    'facility': facility,
    'category': category
})

driver.close()
driver.quit()

