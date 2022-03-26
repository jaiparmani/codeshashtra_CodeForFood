# This will not run on online IDE
import time
import requests
from bs4 import BeautifulSoup

URL = "https://www.hdfcbank.com/personal/pay/cards/debit-cards/debit-cards-offers"
# URL = "https://www.icicibank.com/Personal-Banking/offers/offer-index.page"
# URL = "https://www.icicibank.com/offers/vivo-phones-cashback-offer.page?"
r = requests.get(URL)

# If this line causes an error, run 'pip install html5lib' or install html5lib
soup = BeautifulSoup(r.content, 'html5lib')
a = soup.prettify()
# write a to a file
# with open('data.txt', 'w') as f:
# f.write(a)
# Import Module

# HTML Document
HTML_DOC = """
			<html>
				<head>
					<title> Geeksforgeeks </title>
					<style>.call {background-color:black;} </style>
					<script>getit</script>
				</head>
				<body>
					is a
					<div>Computer Science portal.</div>
				</body>
			</html>
			"""
HTML_DOC = a
# Function to remove tags


def remove_tags(html):

    # parse html content
    soup = BeautifulSoup(html, "html.parser")

    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()

    # return data by retrieving the tag content
    return ' '.join([x+"." for x in (soup.stripped_strings)])


# Print the extracted data
print(remove_tags(HTML_DOC))
