import time
import requests
from bs4 import BeautifulSoup

URL = "https://www.icicibank.com/Personal-Banking/offers/offer-index.page"
r = requests.get(URL)

# If this line causes an error, run 'pip install html5lib' or install html5lib
soup = BeautifulSoup(r.content, 'html5lib')
# link = soup.find_all('span', class_='remaining_time')
# a = soup.find('div', class_='')
# a = soup.find(
# 'div', class_='#offerListWrapper > div:nth-child(1) > div:nth-child(1) > div > div.media')
# print(a.get_text())
# a = soup.find_all('div', class_='offer-card')

# for i in a:
# print(a)
# print(soup)


def remove_tags(html):

    # parse html content
    soup = BeautifulSoup(html, "html.parser")

    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()

    # return data by retrieving the tag content
    return ' '.join([x+"." for x in (soup.stripped_strings)])


print(remove_tags(r))
# # a = soup.prettify()
# # print(type(a))
