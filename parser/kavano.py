import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt
import re

HOST = "https://www.kivano.kg"
URL = "https://www.kivano.kg/elektronika"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='item product_listbox oh')
    anime = []

    for i in items:
        anime.append(
            {
                'title': i.find('div', class_='listbox_title oh').find('a').get_text(),
                'price': re.findall(r'\d+' ,i.find('div', class_='listbox_price text-center').find('strong').get_text())[0],
                'text': i.find('div', class_='product_text pull-left').get_text(),
                'image': HOST + i.find('div', class_='listbox_img pull-left').find('img').get('src'),
                'category': None,
            }
        )
    return anime

html = get_html(URL)
# print(get_data(html))

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            anime.extend(get_data(html.text))
        return anime
    else:
        raise ValueError('Parser error')
