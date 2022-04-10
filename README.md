# Auto Web Scraping: OYO Rooms
*Source: https://www.oyorooms.com/id/hotels-in-yogyakarta/*

<img src='assets/OYO_Rooms_logo.png' alt='OYO Rooms' width='150' height='52'>

## About Project
In this project, I use Selenium to scrape/extract the info of hotels located in **Yogyakarta region, Indonesia**. There were 119 hotels where the information was extracted using this automation script. The extracted information is about:
- Hotel name: name of hotel listed on the website
- Location: location of the hotel
- Rate: rating of the hotel, ranging from 1.0 to 5.0
- Facility: facility offered by the hotel
- Category: category/type of room offered by the hotel

## Python Packages
- webdriver-manager
- selenium
- pandas

## Processes
Broadly speaking, the following process occurs when the script (scrapeOyo.py) is executed.

<img src='assets/Processes.png' alt='Processes'>
<img src='assets/execution_script.gif' alt='Script running'>

## Result
Below is the result as dataframe.
<img src='assets/scraping-result.png' alt='Result'>

Below is the result after saving as CSV.
<img src='assets/scraping-result-2.png' alt='Result'>


