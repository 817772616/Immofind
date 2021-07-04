import requests
from bs4 import BeautifulSoup as bs


RESULTS = []


def fetch_wgg():
    res = requests.get('https://www.wg-gesucht.de/1-zimmer-wohnungen-und-wohnungen-in-Potsdam.107.1+2.1.0.html?sort_column=0&sort_order=0').text
    html = bs(res, 'html.parser')

    for e in html.find_all('div', {'class': 'offer_list_item'}):
        RESULTS.append({
            'title': e.find('h3').get('title'),
            'address': e.find('div', {'class': 'col-xs-11'}).text.strip().replace('\n', '').split('|')[-1].lstrip(),
            'image': e.find('div', {'class': 'card_image'}).a.get('style').split('(')[1][:-2],
            'price': int(e.find('div', {'class': 'col-xs-3'}).text.strip()[:-2]),
            'url': 'https://www.wg-gesucht.de' + e.find('a').get('href')
        })

    return RESULTS
