from bs4 import BeautifulSoup
import requests


# Python でウェブページを解析
html = requests.get('https://www.python.org')

soup = BeautifulSoup(html.text, 'lxml')

titles = soup.find_all('title')
print(titles)
print(titles[0].text)

intro = soup.find_all('div', {'class': 'introduction'})
print(intro)
print(intro[0].text)