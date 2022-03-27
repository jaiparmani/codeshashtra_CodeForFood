from django.shortcuts import render
# import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Users, CardType, Card, OfferCategory, OfferDetails, Offer
from twilio.rest import Client
import imaplib
import email
import http.client
import wordninja
import json
from bs4 import BeautifulSoup
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def homePage(request):
    return render(request, "home.html", {})


def getDetails(image):
    cardNumber = "123456789"
    bankName = "ICICI"
    cardCategory = "Gold Debit"
    return cardNumber, bankName, cardCategory


def uploadCard(request):
    if request.method == 'POST':
        image = request.POST.get('cardImage')

        if(not request.POST.get('cardCategory')):
            cardNumber, bankName, cardCategory = getDetails(image)

            return render(request, "uploadCard.html", {"cardNumber": cardNumber, "bankName": bankName, "cardCategory": cardCategory})
        else:
            cardNumber = request.POST.get('cardNumber')
            bankName = request.POST.get('bankName')
            cardCategory = request.POST.get('cardCategory')
            user = request.username
            user = Users.objects.get(username=user)
            card = Card(user=user, card_number=cardNumber,
                        card_type=cardCategory)
            return render(request, "uploadCard.html", {})
        # if form.is_valid():
        #     form.save()
        #     return HttpResponse('File uploaded')
        # else:
        #     return HttpResponse('Invalid File')
    else:

        return render(request, 'uploadCard.html', {})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Users.objects.get(username=username)
        if user.password == password:
            return render(request, "home.html", {})
        else:
            return render(request, "login.html", {})
    else:
        return render(request, "login.html", {})


def offerList(request):
    if request.method == 'POST':
        offerId = request.POST.get('offerId')
        offer = Offer.objects.get(id=offerId)
        return render(request, "offerDetails.html", {"offer": offer})
    else:
        offerList = Offer.objects.all()
        # group offers according to category
        offerCategory = {}
        for offer1 in offerList:
            offer = {"offerID": offer1.offerID, "offerTitle": offer1.offerTitle, "offerSource": offer1.offerSource, "offerDescription": offer1.offerDescription,
                     "offerImage": offer1.offerImage, "offerLink": offer1.offerLink, "offerPrice": offer1.offerPrice, "offerCategory": offer1.offerCategory}
            offer, offer1 = offer1, offer
            try:
                print("HELLO", len(offer1['offerImage']))
            except:
                pass
            if offer.offerCategory.category in offerCategory:
                offerCategory[offer.offerCategory.category].append(offer1)
            else:
                offerCategory[offer.offerCategory.category] = [offer1]
        print(offerCategory)    
        return render(request, "offerList.html", {"offerCategory": offerCategory, "foodOffers":offerCategory['food'], "entertainmentOffers":offerCategory['entertainment'], 'clothesOffers':offerCategory['clothes']})


# def offerDetails(request):

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele
        str1 +=' '  
    
    # return string  
    return str1 

def getPampletData(request):
    if request.method == "POST":
        import ast
        import json
        import requests
        url = 'https://app.nanonets.com/api/v2/OCR/Model/4324c647-72a7-4bb8-bb9e-e5068f3acb2e/LabelFile/'

        data = {'file': open('ocrtest.jpg', 'rb')}

        response = requests.post(url, auth=requests.auth.HTTPBasicAuth(
            '3MjnNJP7BOApdrHAUKMbeaRIVJn43Kn2', ''), files=data)
        # print((response.text))
        res = ast.literal_eval(response.text)
        msg = (res['result'][0]['prediction'][0]['ocr_text'])
        msglist=wordninja.split(msg)
        str = (listToString(msglist))
        obj = Offer(user = request.user, offerTitle=str)
        obj.save()
        return HttpResponse("OFFER INSERTED")

    else:
        return render(request, "pampletData.html", {})


def registerCard(request):
    if request.method == "POST":

        image = request.post.get("debitCardImage")

        if(not request.post.get("cardNumber")):
            # get ocr
            import requests

            url = 'https://app.nanonets.com/api/v2/OCR/Model/cee854ec-bd62-4521-8fc8-7be009f44583/LabelFile/'
            # d
            data = {'file': open("./images.jpg", 'rb')}

            response = requests.post(url, auth=requests.auth.HTTPBasicAuth(
                '3MjnNJP7BOApdrHAUKMbeaRIVJn43Kn2', ''), files=data)

            print(response.text)

        else:
            cardNumber = request.post.get("cardNumber")
            bankName = request.post.get("bankName")
            cardType = request.post.get("cardType")
            obj = Card(cardNumber=cardNumber,
                       bankName=bankName, cardType=cardType)
            obj.save
            return render(request, "home.html")

    else:
        return render(request, "registerCard.html")

def sendWhatsappAlert(request):
    
    account_sid = "AC2b86506e501303ebd8ed51b450aa5654"
    auth_token  = "440c92695a3b38d817e8c28ea276eabe"

    client = Client(account_sid, auth_token)

    # this is the Twilio sandbox testing number
    from_whatsapp_number='whatsapp:+14155238886'
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number='whatsapp:+919004525005'
    import datetime
    nextWeek = datetime.datetime.now() + datetime.timedelta(days = 7)
    expiringOffers = Offer.objects.all().filter(offerValidUpto__lte = nextWeek)
    msg = "Coupons that are about to expire:\n"
    for i in range(len(expiringOffers)):
        msg += str(i+1)+". "+str(expiringOffers[i].offerTitle)
    
    client.messages.create(body=msg,
                        from_=from_whatsapp_number,
                        to=to_whatsapp_number)
    


def getOffersFromMail():
    my_email="codeforfood26@gmail.com"
    my_pass="Codeforfood@26"
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(my_email,my_pass)
    mail.select("inbox") 
    mails=[]
    result, data = mail.search(None,'ALL')
    if result == 'OK':
        for num in data[0].split():
            result, data = mail.uid('fetch', num, '(RFC822)')
            if result == 'OK':
                try:
                    email_message = email.message_from_bytes(data[0][1])
                # print(email_message['Subject'])
                except:
                    continue
                if('upto' in email_message['Subject'] and '%' in email_message['Subject']):
                    flag=1
                elif('discount' in email_message['Subject']):
                    flag=1
                else:
                    flag=0
                if flag==1:
                    mails.append(email_message['Subject'])
    
    for i in mails:
        obj = Offer(offerTitle = i)
        obj.save()
    return HttpResponse(mails)

def getDiscountsOfProduct(request):
    conn = http.client.HTTPSConnection("magic-scraping.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Host': "magic-scraping.p.rapidapi.com",
        'X-RapidAPI-Key': "2793865f9fmsh57d5d6fd6a814fcp106418jsna07ae6c4acca"
        }

    conn.request("GET", "/api/v2/scrapping?url=https%3A%2F%2Fcashkaro.com%2Fsearch%2Fiphone%2B12", headers=headers)

    res = conn.getresponse()
    data = res.read()
    data=data.decode("utf-8")
    datalist=wordninja.split(data)
    final_dictionary = json.loads(data)
    keys = (final_dictionary.keys())
    pagecontent=final_dictionary['pageContentHTML']
    soup = BeautifulSoup(pagecontent, 'html5lib')
    products=[]
    prices=[]
    strikes=[]
    finalp=[]
    texts=(soup.find_all("a", class_="product_name"))
    for text in texts:
        products.append(text.get_text())
    texts=(soup.find_all("span", class_="price_strike"))
    for text in texts:
        strikes.append(text.get_text())
    texts=(soup.find_all("span", class_="p_totalprice"))
    for text in texts:
        val=text.get_text()
        prices.append(val[val.index("₹")+1:])
    texts=(soup.find_all("p", class_="fl fw"))
    for text in texts:
        val=text.get_text()
        finalp.append(val[val.index("₹")+1:])
    print(products)
    print(strikes)
    print(prices)
    print(finalp)
    discount=[]
    for i in range(len(finalp)):
        discount.append(int(prices[i].replace(',',''))-int(finalp[i].replace(',','')))
    print(discount)

