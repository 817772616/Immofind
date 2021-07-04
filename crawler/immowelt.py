import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs


options = Options()
options.headless = True
RESULTS = []


def fetch_immowelt():
    driver = webdriver.Chrome(options=options, executable_path='./static/chromedriver')
    driver.maximize_window()
    driver.get('https://www.immowelt.de/liste/potsdam/wohnungen/mieten?roomi=2&rooma=2&sort=createdate%2Bdesc')
    time.sleep(3)

    # identify cookie-banner in shadow-DOM
    shadow_root = driver.find_element(By.CSS_SELECTOR, "div[role='region']")
    last = driver.execute_script('return arguments[0].shadowRoot', shadow_root)
    time.sleep(3)
    accept = last.find_element(By.CSS_SELECTOR, "button[aria-label='Alles akzeptieren']")
    accept.click()
    time.sleep(1)
    driver.refresh()

    last_height = driver.execute_script("return document.body.scrollHeight")
    # Scroll to bottom to get all results
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height

    # Parse HTML
    time.sleep(1)
    items = driver.find_element(By.XPATH, "//div[@id='listItemWrapperAsync']")
    html = bs(items.get_attribute('innerHTML'), 'html.parser')
    driver.close()

    # Identify data
    for e in html.find_all('div', {'class': 'js-listitem'}):
        title = e.find('h2', {'class': 'ellipsis'}).text

        price = int(e.find('strong').text.strip()[:-2].replace('.', '').split(',')[0])
        image = e.find('img').get('srcset').split(',')[0][:-4]
        address = e.find('div', {'class': 'listlocation'}).text.strip()
        link = e.find('a').get('href')

        RESULTS.append({
            'title': title,
            'price': price,
            'image': image,
            'address': address,
            'url': 'https://www.immowelt.de' + link
        })

    return RESULTS
