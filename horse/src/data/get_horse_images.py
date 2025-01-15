import os
import requests
from bs4 import BeautifulSoup
import json
import urllib
from time import sleep

with open('horse_breeds.json', 'r') as f:
    breeds = json.load(f)

os.makedirs('horse_images', exist_ok=True)

for breed in breeds:
    print(f"Proccessing {breed['Name']}")
    try:
        horse_page = requests.get(breed['Link'], headers={'User-Agent': 'HorseBreedDisplayer/1.0 (soumyab550@gmail.com)'})
        horse_soup = BeautifulSoup(horse_page.text, 'html.parser')

        infobox_image = horse_soup.find('td', class_='infobox-image')
        # infobox = horse_soup.find_all('table', class_='infobox biota')
        if infobox_image:
            image = infobox_image.find('img')
            print(image['src'])
            if image:
                image_url = f"https:{image['src']}"
                print()
                print(image_url)
                filename = f"horse_images/{breed['Name'].replace(' ', '_')}.jpg"
                urllib.request.urlretrieve(image_url, filename)

                breed['Image'] = f"/data/"+filename
                breed['ImageURL'] = image_url
            else:
                breed['Image'] = None
                breed['ImageURL'] = None
        else:
            breed['Image'] = None
            breed['ImageURL'] = None

    except Exception as e:
        print(f"Failed to get image for {breed['Name']}: {e}")
        breed['Image'] = None
        breed['ImageURL'] = None
    sleep(0.3)


with open('horse_breed_imgs.json', 'w') as f:
    json.dump(breeds, f, indent=4)