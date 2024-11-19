import os
import requests
from bs4 import BeautifulSoup
import json

with open('horse_breeds.json', 'r') as f:
    breeds = json.load(f)

os.makedirs('horse_images', exist_ok=True)

for breed in breeds:
    print('Processing: ', breed['Name'])
    try:
        horse_page = requests.get(breed['Link'])
        horse_soup = BeautifulSoup(horse_page.text, 'html.parser')

        infobox_image = horse_soup.find('td', class_='infobox-image')
        if infobox_image:
            image = infobox_image.find('img')
            if image:
                image_url = f"https:{image['src']}"
                image_data = requests.get(image_url).content
                filename = f"horse_images/{breed['Name'].replace(' ', '_')}.jpg"
                with open(filename, 'wb') as img_file:
                    img_file.write(image_data)
                
                breed['Image'] = filename
            else:
                breed['Image'] = None
        else:
            breed['Image'] = None

    except Exception as e:
        print(f"Failed to get image for {breed['Name']}: {e}")
        breed['Image'] = None


with open('horse_breed_imgs.json', 'w') as f:
    json.dump(breeds, f, indent=4)