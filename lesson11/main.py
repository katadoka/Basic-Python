# Parser for https://docs.python.org/3/
from collections import namedtuple

import requests
from bs4 import BeautifulSoup


BASE_URL = 'https://docs.python.org/3/'
UrlObject = namedtuple('UrlObject', ['name', 'url'])


def print_links(links):
    for c, link in enumerate(links, 1):
        print(f'{c}. {link.name}: {link.url}')


def search_links(url=BASE_URL, search_key='table a'):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = [UrlObject(a.text, BASE_URL + a.get('href')) for a in soup.select(search_key)]
    return links


def link_use(links, link_number):
    link = links[link_number-1]
    page_links = search_links(url=link.url, search_key='a')
    print_links(page_links)


links = search_links()
print_links(links)
link_number = int(input("Enter the link number: "))
link_use(links, link_number)
