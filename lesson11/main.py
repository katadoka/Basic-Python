# Parser for https://docs.python.org/3/


import requests
from bs4 import BeautifulSoup


def search_links(links):
    counter = 0
    for link in links:
        counter += 1
        print(f'{counter}. {link.text}: {BASE_URL}{link.get("href")}')

def link_use(links):
    counter = 0
    for link in links:
        counter += 1
        if link_number == counter:
            b = link.get('href')
            response_link = requests.get(BASE_URL + b)
            soup_link = BeautifulSoup(response_link.content, 'html.parser')
            counter_link = 0
            for link in soup_link.find_all('a'):
                counter_link += 1
                print(f'{counter_link}. {link.text}: {BASE_URL}{link.get("href")}')


BASE_URL = 'https://docs.python.org/3/'
response = requests.get(BASE_URL)

soup = BeautifulSoup(response.content, 'html.parser')

links = []
counter = 0
for table in soup.find_all('table'):
    links += table.find_all('a')

search_links(links)

link_number = int(input("Enter the link number: "))

link_use(links)
