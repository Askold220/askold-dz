import requests
from bs4 import BeautifulSoup

base_url = 'https://quotes.toscrape.com'
page_number = 1
quotes = []

while True:
    response = requests.get(f'{base_url}/page/{page_number}/')
    soup = BeautifulSoup(response.content, 'html.parser')
    
    quotes_on_page = soup.select('.quote')
    
    if not quotes_on_page:
        break
    
    for quote in quotes_on_page:
        text = quote.select_one('.text').get_text()
        author = quote.select_one('.author').get_text()
        tags = [tag.get_text() for tag in quote.select('.tags .tag')]
        
        quotes.append({
            'text': text,
            'author': author,
            'tags': tags
        })
    
    page_number += 1

for index, quote in enumerate(quotes, start=1):
    with open(f'data/quote{index}.txt', 'w', encoding='utf-8') as file:
        file.write(f"Quote: {quote['text']}\nAuthor: {quote['author']}\nTags: {', '.join(quote['tags'])}\n\n")
