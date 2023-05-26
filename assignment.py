import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://vesti.kg/'

def write_to_csv(data):
    with open('newsstitle.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['link']])

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    list_news = soup.find_all('div', class_ = 'itemBody')
    for news in list_news:
        title = news.find('h2').text.strip()
        search = 'https://vesti.kg/' + news.a.get('href')
        dict_ = {'title':title, 'link':search}
        write_to_csv(dict_)

def main():
    count = 0
    for i in range(100):
        news_url = f'https://vesti.kg/itemlist.html?start={str(count)}'
        get_data(get_html(news_url))
        count += 30

main()