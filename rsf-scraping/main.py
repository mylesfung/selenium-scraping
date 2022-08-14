# Mission: scrape RSF Meter and send capacity data to Google Sheet every 15 minutes.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
from datetime import datetime
import time

import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials

driver = webdriver.Chrome(
    executable_path='/Users/myles/Desktop/Main/selenium-scraping/chromedriver',
    service=Service(ChromeDriverManager().install())
)

capacities = []

#def add_capacity():
URL = 'https://safe.density.io/#/displays/dsp_956223069054042646?token=shr_o69HxjQ0BYrY2FPD9HxdirhJYcFDCeRolEd744Uj88e'
driver.get(URL)

when = datetime.now().strftime('%m/%d/%Y %H:%M')
cap = driver.find_element(By.XPATH, './/*[@id="root"]/div/div/div[1]/div[2]/div/span')
row = {
    'Date and Time': when,
    'Capacity': cap
}
capacities.append(row)