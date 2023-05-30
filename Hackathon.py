# ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: средняя)
# ● Спарсить mashina.kg, категорию:
# 1.Название всех моделей.
# 2.Цену всех моделей
# 3.Изображение всех моделей
# 4.Краткое описание всех моделей
# 5.Записать все в csv файл

# ● Библиотеки, которыми вы должны воспользоваться:
# BeautifulSoup4
# csv
# requests

from bs4 import BeautifulSoup
import requests
import csv

def write_csv(data):
    with open('mashina.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([data['title'], data['price'], data['description'], data['image']])    
def get_html(url):
    respone = requests.get(url).text
    return respone

def news(html):
    soup = BeautifulSoup(html, 'lxml')
    list_ = soup.find_all('div', class_= 'list-item list-label')
    for car in list_:
        title = car.find('h2', class_='name').text.replace('\n', '').strip()
        price = car.find('p').text.replace('\n', '').strip()
        image = car.find('img', class_='lazy-image').get('data-src')
        description = car.find('div', class_ = 'block info-wrapper item-info-wrapper').text.replace('\n', '').replace(' ','').replace(',', '')
        dict_ = {'title':title, 'price':price, 'description':description, 'image':image}
        write_csv(dict_)

def main():
    for i in range(1,10):
        url = f'https://www.mashina.kg/search/all/?page={i}'
        news(get_html(url))

main()

