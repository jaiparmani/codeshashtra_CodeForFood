from django.shortcuts import render
# import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Users, CardType, Card, OfferCategory, OfferDetails, Offer
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
            if offer.offerCategory.category in offerCategory:
                offerCategory[offer.offerCategory.category].append(offer1)
            else:
                offerCategory[offer.offerCategory.category] = [offer1]
        print(offerCategory)
        return render(request, "offerList.html", {"offerCategory": offerCategory})


# def offerDetails(request):


def getPampletData(request):
    if request.method == "POST":
        pass
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
