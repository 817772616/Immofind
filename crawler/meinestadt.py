import requests
import json


RESULTS = []


def fetch_meinestadt():
    data = {
        'geoid': 108,
        'pageSize': 20,
        'page': 1,
        'lat': 52.4253,
        'lng': 13.0006,
        'location': 'potsdam',
        'esr': 2,
        'etype': 1,
        'sort': 'createdate+desc',
        'sr': 20,
        'bigimage': 'true',
        'roomi': 0,
        'flmi': 0,
        'primi': 0,
        'isPriceOnRequest': 'false',
        'debug': 'false',
        'usersSort': 'true',
        'userModified': 'true'
    }
    headers = {
        'Origin': 'https://www.meinestadt.de',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
    }

    res = requests.get('https://www.meinestadt.de/potsdam/immobilien?service=immoweltAjax', data=data, headers=headers).text
    raw = json.loads(res)

    for i in raw['searchboxResults']['items']:
        RESULTS.append({
            'title': i['title'],
            'url': i['detailUrl'],
            'image': i['smallImageUrl'],
            'street': i['street'],
            'plz': i['postcode'],
            'price': int(i['priceRaw']),
            'date': i['createdDateFormatted']
        })

    return RESULTS
