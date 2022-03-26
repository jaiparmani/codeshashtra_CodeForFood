import requests

url = 'https://app.nanonets.com/api/v2/OCR/Model/cee854ec-bd62-4521-8fc8-7be009f44583/LabelFile/'
# d
data = {'file': open("./images.jpg", 'rb')}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth(
    '3MjnNJP7BOApdrHAUKMbeaRIVJn43Kn2', ''), files=data)

print(response.text)
