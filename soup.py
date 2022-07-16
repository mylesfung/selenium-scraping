#import requests
#from bs4 import BeautifulSoup

# Dynamic scraping using automated web browser with selenium.
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/myles/desktop/projects/tasting-the-soup/chromedriver')
driver.get('https://www.youtube.com/c/JordanPetersonVideos/videos?view=0&sort=dd&flow=grid')

videos = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-grid-video-renderer')

for video in videos:
    title = video.find_element(By.XPATH, './/*[@id="video-title"]').text
    views = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text
    posted = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[2]').text
    length = video.find_element(By.XPATH, './/*[@id="text"]').text
    print(title, views, posted, length)





