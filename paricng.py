'=====================Parcing======================='
# parring - process of aumatic sbora dof data 

# Liabriries:
# 1. requests - send request to website and gets html code of the page
# 2. Beautifulsoup4 - helps izvlech' info from html. Also helps to obrazhatsya k opredelennym tags and get info
# 3 lxml - vystupaet v roli parcera for BS (razbivaet info on small pieces and analyse data)

# python3 -m venv venv - create virtual okrujenie
# source venv/bin/acivate - activates virtual okrujenie
# . venv/bin/acivate

import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://enter.kg/computers/noutbuki_bishkek'

def write_to_csv(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['price'], data['image']])
def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    list_comp = soup.find_all('div', class_ = 'row')
    for comp in list_comp:
        title = comp.find('span', class_ = 'prouct_name').text
        price = comp.find('span', class_ = 'price').text
        image = 'https://enter.kg' + comp.find('img').get('src')
        dict_ = {'title':title, 'price':price, 'image':image}
        write_to_csv(dict_)

print(get_data(get_html(URL)))
