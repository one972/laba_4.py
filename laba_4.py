import requests
from bs4 import BeautifulSoup
import re  

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    
    russian_quotes = []
    
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        
        if re.search('[а-яА-Я]', text):
            russian_quotes.append((text, author))  
    
    russian_quotes.sort(key=lambda x: x[0])  
    for index, (text, author) in enumerate(russian_quotes, start=1):
        print(f'{index}. Цитата: {text}\nАвтор: {author}\n')
else:
    print(f'Ошибка: не удалось получить данные. Статус код: {response.status_code}')
