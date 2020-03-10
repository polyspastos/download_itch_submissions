'''
i did it with firefox, but should be trivial to change it to chrome if you prefer that
pip install bs4
pip install selenium
get the webdriver from here and put it in the same directory as the script (or put it in PATH):
https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win64.zip
'''
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from time import sleep


response = requests.get('https://itch.io/jam/lux-jam/entries')
soup = BeautifulSoup(response.text, features="lxml")
a_tags = soup.find_all('a')

aggregated_links = []
for res in a_tags:
    link = res.get('href')

    if isinstance(link, str):
        if 'itch.io/' in link and link not in aggregated_links:
            aggregated_links.append(link)

browser = webdriver.Firefox()
for second_level_link in aggregated_links:
    try:
        browser.get(second_level_link)
        browser.execute_script("document.getElementsByClassName('button download_btn')[0].click()")
        sleep(1.2)
    except Exception as e:
        print(e)