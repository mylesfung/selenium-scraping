# Dynamic scraping using selenium-automated Chrome browser.
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(executable_path='/Users/myles/desktop/projects/tasting-the-soup/chromedriver')
url = 'https://www.youtube.com/c/JordanPetersonVideos/videos?view=0&sort=p&flow=grid'
driver.get(url)

placards = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-grid-video-renderer')
all_videos = []

for placard in placards:
    title = placard.find_element(By.XPATH, './/*[@id="video-title"]').text
    views = placard.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text
    posted = placard.find_element(By.XPATH, './/*[@id="metadata-line"]/span[2]').text
    length = placard.find_element(By.XPATH, './/*[@id="text"]').text                           

    video_data = {
        'Title': title,
        'Views': views,
        'Time Posted': posted,
        'Length': length
    }
    all_videos.append(video_data)

df = pd.DataFrame(all_videos)
print(df)





