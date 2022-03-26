import json
import http.client

conn = http.client.HTTPSConnection("magic-scraping.p.rapidapi.com")

headers = {
    'X-RapidAPI-Host': "magic-scraping.p.rapidapi.com",
    'X-RapidAPI-Key': "5864663690msh5ece893f9fe231fp10ec05jsn009193f8dd78"
}

conn.request(
    "GET", "/api/v2/scrapping?url=https://cashkaro.com/search/iphone+12", headers=headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
op = data.decode("utf-8")
op = op.split(',')
# Python program to read
# json file


# Opening JSON file

f = open('data.txt',)
# returns JSON object as
# a dictionary
data = json.dump(f, op)

# Iterating through the json
# list

# Closing file
f.close()
