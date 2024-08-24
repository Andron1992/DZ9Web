import requests
from bs4 import BeautifulSoup
import json
import time


def scrape_quotes():
    base_url = "http://quotes.toscrape.com"
    quotes = []
    authors = {}

    page = 1
    while True:
        url = f"{base_url}/page/{page}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        quotes_list = soup.find_all('div', class_='quote')
        if not quotes_list:
            break

        for quote_div in quotes_list:
            quote_text = quote_div.find('span', class_='text').get_text()
            author_name = quote_div.find('small', class_='author').get_text()
            author_url = quote_div.find('a')['href']

            quotes.append({
                'text': quote_text,
                'author': author_name
            })

            if author_url not in authors:
                author_page_url = base_url + author_url
                author_response = requests.get(author_page_url)
                author_soup = BeautifulSoup(author_response.text, 'html.parser')
                birth_date = author_soup.find('span', class_='author-born-date').get_text()
                birth_location = author_soup.find('span', class_='author-born-location').get_text()
                description = author_soup.find('div', class_='author-description').get_text()

                authors[author_url] = {
                    'name': author_name,
                    'birth_date': birth_date,
                    'birth_location': birth_location,
                    'description': description
                }

        page += 1
        time.sleep(1)

    with open('quotes.json', 'w', encoding='utf-8') as f:
        json.dump(quotes, f, ensure_ascii=False, indent=4)

    with open('authors.json', 'w', encoding='utf-8') as f:
        json.dump(authors, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    scrape_quotes()
