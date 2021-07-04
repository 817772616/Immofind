import requests
from bs4 import BeautifulSoup as bs


RESULTS = []


def fetch_ebay():
    headers = {
        'Origin': 'https://www.ebay-kleinanzeigen.de',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
    }

    res = requests.get('https://www.ebay-kleinanzeigen.de/s-wohnung-mieten/potsdam/2-zimmer-wohnung/k0c203l7958', headers=headers).text
    html = bs(res, 'html.parser')

    for i in html.find_all('article', {'class': 'aditem'}):
        RESULTS.append({
            'plz': i.find('div', {'class': 'aditem-main--top--left'}).text.strip(),
            'title': i.find('a', {'class': 'ellipsis'}).text,
            'link': 'https://www.ebay-kleinanzeigen.de' + i.find('a', {'class': 'ellipsis'}).get('href'),
            'price': i.find('p', {'class': 'aditem-main--middle--price'}).text.strip().split(' ')[0].replace('.', ''),
            'image': i.find('div', {'class': 'imagebox'}).get('data-imgsrc'),
        })

    return RESULTS
