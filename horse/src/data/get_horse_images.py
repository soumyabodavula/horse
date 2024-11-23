import os
import requests
from bs4 import BeautifulSoup
import json
import urllib

with open('horse_breeds.json', 'r') as f:
    breeds = json.load(f)

os.makedirs('horse_images', exist_ok=True)

for breed in breeds:
    print(f"Proccessing {breed['Name']}")
    try:
        horse_page = requests.get(breed['Link'])
        horse_soup = BeautifulSoup(horse_page.text, 'html.parser')

        infobox_image = horse_soup.find('td', class_='infobox-image')
        # infobox_image = horse_soup.find_all('table', class_='infobox biota')
        print(infobox_image)
        if infobox_image:
            image = infobox_image.find('img')
            print(image['src'])
            if image:
                image_url = f"https:{image['src']}"
                print()
                print(image_url)
                fn = f"{breed['Name'].replace(' ', '_')}.jpg"
                filename = f"horse_images/{breed['Name'].replace(' ', '_')}.jpg"
                print(fn)
                urllib.request.urlretrieve(image_url, filename)
                image_data = requests.get(image_url).content
                
                # with open(filename, 'wb') as img_file:
                #     img_file.write(image_data)
                
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


with open('horse_breed_imgs.json', 'w') as f:
    json.dump(breeds, f, indent=4)