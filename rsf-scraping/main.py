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


## Crawler and Scraper ##

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

row_data = []


#def add_row():
URL = 'https://safe.density.io/#/displays/dsp_956223069054042646?token=shr_o69HxjQ0BYrY2FPD9HxdirhJYcFDCeRolEd744Uj88e'
driver.get(URL)
time.sleep(10)

date_time = datetime.now().strftime('%m/%d/%Y %H:%M')
cap = driver.find_element(By.XPATH, './/*[@id="root"]/div/div/div[1]/div[2]/div/span').text

'''row = {
    'Date and Time': date_time,
    'Capacity': cap
}
row_data.append(row)

df = pd.DataFrame(data=row_data)
#print(df)'''


## Authentication and Upload ##

SCOPE = [
    #'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
    #'https://www.googleapis.com/auth/drive.file'
    'https://www.googleapis.com/auth/spreadsheets'
]

creds = ServiceAccountCredentials.from_json_keyfile_name('secret-key.json', SCOPE)
client = gspread.authorize(creds)

spreadsheet = client.open_by_key('1x1JomLFPq3CShupUfJW60zzBmispI2-yzIbndF3skVk').Main
spreadsheet.append_row([date_time, cap])