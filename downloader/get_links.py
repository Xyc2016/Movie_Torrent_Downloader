import requests
from bs4 import BeautifulSoup

import bs4


def get_soup(url)->BeautifulSoup:
    return BeautifulSoup(requests.get(url).content, 'html.parser')


def get_search_results(url):
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    l0 = soup.find_all(
        'a', class_='so_pic'
    )

    return ['http://www.btbtdy.com' + node['href'] for node in l0
                if node['href'].split('/')[-1].split('.')[0][2:].__len__()==4
            ]


def _get_download_links(url):
    url0 = url.replace('btdy/dy','vidlist/')
    soup = get_soup(url0)
    # return [ node['href'] for node in soup.find_all('a','d1') ]
    lis = soup.find_all('li')
    l = []
    for li in lis:
        v = (
            list(li.children)[0]['title'],list(list(li.children)[1].children)[0]['href']
        )
        l.append(v)
    return l


def get_download_urls(url):

    l0 = get_search_results(url)
    l1 = []
    for url in l0:
        l1.extend(
            _get_download_links(url)
        )
    return l1




