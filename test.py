import os
from pprint import pprint

from bs4 import BeautifulSoup
import requests

SEARCH_TERM = 'education'
FILE_TO_SAVE_TO = 'content.txt'
API_KEY = os.environ['API_KEY']

API_URL = f'https://newsapi.org/v2/everything?q={SEARCH_TERM}&from=2021-02-11&sortBy=publishedAt&apiKey={API_KEY}'

r = requests.get(API_URL)

articles = r.json()['articles']

print("here's an example of one of the things that comes back from the API")
print(articles[0])

list_of_urls = [article['url'] for article in articles]

# uncomment the line below to see the list of urls for the articles
#print(list_of_urls)
for url in list_of_urls:

    response = requests.get(url)

    content = response.content

    soup = BeautifulSoup(content, features="html.parser")

    just_text = soup.get_text().strip()
    # uncomment the line below to see the full text coming back
    #print(just_text)

    with open(f'{FILE_TO_SAVE_TO}', 'a') as output_file:
        output_file.write(just_text)
        output_file.write('\n')
