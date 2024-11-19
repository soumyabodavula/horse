import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os

url = 'https://en.wikipedia.org/wiki/List_of_horse_breeds'

try:
    page = requests.get(url)
    page.raise_for_status()
except Exception as e:
    print('Error downloading page!!!: ', e)
    exit()

soup = BeautifulSoup(page.text, 'html.parser')

div_cols = soup.find_all('div', class_='div-col')
horses = []
count = 0
while count < 4:
    horse_list = div_cols[count].find_all('li')
    for li in horse_list:
        name = li.text.strip()
        link = li.find('a')
        horse_link = f"https://en.wikipedia.org{link['href']}" if link else None
        horses.append({'Name': name, 'Link': horse_link})
    count+=1

with open('horse_breeds.json', 'w') as f:
    json.dump(horses, f, indent=4)



