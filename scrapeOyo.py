from unicodedata import category
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True) # Avoiding browser for closing after opened
opt.add_argument('--ignore-certificate-errors') # Handle node connection error (0x1F)
opt.add_argument("--disable-webgl")
opt.add_argument("--disable-notifications") # Disable browser push notification
opt.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
driver.implicitly_wait(15)
driver.get('https://www.oyorooms.com/id/hotels-in-yogyakarta/')
driver.maximize_window()

# Get url for all pages (href attributes)
page_url = [url.get_attribute('href') for url in driver.find_elements(By.CLASS_NAME, 'ListingPagination__pageContainer--page')]

# Get url for all hotels
hotel_url = []
for page in page_url:
    driver.get(page)
    hotel_url.extend(url.get_attribute('href') for url in driver.find_elements(By.CSS_SELECTOR, 'div.listingHotelDescription__contentWrapper--left > a.c-nn640c'))

hotel_name = []
location = []
rate = []
facility = []
category = []
# Scrape hotel info, page by page
for url in hotel_url:
    driver.get(url)
    print('Scraping... ' + str(hotel_url.index(url)+1) + ' of ' + str(len(hotel_url)) + " hotels")
    hotel_name.append(driver.find_element(By.CSS_SELECTOR, 'h1.c-1wj1luj').text)
    location.append(driver.find_element(By.CSS_SELECTOR, '[itemprop="streetAddress"]').text)
    facility.append(', '.join([i.text for i in driver.find_elements(By.CSS_SELECTOR, 'div.c-12w6zty')]))
    category.append(', '.join([i.text for i in driver.find_elements(By.CSS_SELECTOR, 'span.c-2j9z2q')]))
    # Some hotels are unrated yet/NEW, there for:
    try:
        rate.append(driver.find_element(By.CSS_SELECTOR, 'div.c-186t5ao').text)
    except NoSuchElementException:
        rate.append('NEW')

# Compile info as dataframe
hotel_df = pd.DataFrame({
    'hotel_name': hotel_name,
    'location': location,
    'rate': rate,
    'facility': facility,
    'category': category
})

hotel_df.to_csv('OYO-hotel-Yogyakarta.csv')

driver.close()
driver.quit()

