import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://safe.density.io/#/displays/dsp_956223069054042646?token=shr_o69HxjQ0BYrY2FPD9HxdirhJYcFDCeRolEd744Uj88e'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')

'''
browser = webdriver.Chrome()
browser.get('https://safe.density.io/#/displays/dsp_956223069054042646?token=shr_o69HxjQ0BYrY2FPD9HxdirhJYcFDCeRolEd744Uj88e')
print(browser.title)
browser.quit()'''

# alternatively pass in an open(filehandle)
'''
with open('index.html') as markup:
    first_soup = BeautifulSoup(markup, 'lxml')
'''