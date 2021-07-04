import requests
from bs4 import BeautifulSoup as bs


RESULTS = []


def fetch_nestoria():
    res = requests.get('https://www.nestoria.de/immobilien/mieten/potsdam?bedrooms=1,2&sort=newest').text
    html = bs(res, 'html.parser')

    for e in html.find_all('li', {'class': 'rating__new'}):
        url = 'https://www.nestoria.de' + e.find('a').get('data-href')
        title = e.find('div', {'class': 'listing__title__text'}).text.strip()
        image = e.find('img', {'class': 'image_click_origin'}).get('data-lazy')

        try:
            price = int(e.find('div', {'class': 'result__details__price'}).text.strip().split(' ')[0])
        except ValueError:
            price = int(e.find('div', {'class': 'result__details__price'}).text.strip().split(' ')[0].replace('.', ''))

        RESULTS.append({
            'url': url, 'title': title, 'image': image, 'price': price
        })

    return RESULTS
