from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

import gspread
from oauth2client.service_account import ServiceAccountCredentials


#######################
# Crawler and Scraper #
#######################

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def add_row_data():
    try:
        URL = 'https://safe.density.io/#/displays/dsp_956223069054042646?token=shr_o69HxjQ0BYrY2FPD9HxdirhJYcFDCeRolEd744Uj88e'
        driver.get(URL)
        time.sleep(5)

        capacity = driver.find_element(By.XPATH, './/*[@id="root"]/div/div/div[1]/div[2]/div/span').text[0]
        date_time = time.ctime()[:4] + time.strftime('%m/%d/%Y %H:%M')
        #date_time = time.ctime()[:16]
        
        spreadsheet.append_row([date_time, capacity])
    except Exception as e:
        print(f'Density Display Load Error: {e}')


#################
# Authorization #
#################

SCOPE = [
    #'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/spreadsheets'
    #'https://www.googleapis.com/auth/drive',
    #'https://www.googleapis.com/auth/drive.file'
]

creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/myles/desktop/main/keys/rsf-key.json', SCOPE)
client = gspread.authorize(creds)
spreadsheet = client.open_by_key('1x1JomLFPq3CShupUfJW60zzBmispI2-yzIbndF3skVk').sheet1


########
# Loop #
########

# Due to the initial sleep period, each timestamp will be 
# staggered from the previous by approximately 6 seconds.
minute_intervals = 10

while True:
    add_row_data()
    time.sleep((60 * minute_intervals))