#!/usr/bin/env python3
from crawler.ebay import fetch_ebay
from crawler.meinestadt import fetch_meinestadt
from crawler.wgg import fetch_wgg
from crawler.immowelt import fetch_immowelt
from crawler.nestoria import fetch_nestoria
import json


def crawl():
    results = {}
    with open('./static/output.json', 'w') as out:

        results['ebay'] = fetch_ebay()
        results['ms'] = fetch_meinestadt()
        results['wgg'] = fetch_wgg()
        results['iw'] = fetch_immowelt()
        results['nest'] = fetch_nestoria()

        out.write(json.dumps(results))


if __name__ == '__main__':
    crawl()