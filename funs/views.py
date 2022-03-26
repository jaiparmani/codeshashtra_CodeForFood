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
    cardCategory = "Gold Debit "
    return cardNumber, bankName, cardCategory


def uploadCard(request):
    if request.method == 'POST':
        image = request.POST['cardImage']
        if(request.POST['cardCategory'] == None):
            cardNumber, bankName, cardCategory = getDetails(image)

            return render(request, "uploadCard.html", {"cardNumber": cardNumber, "bankName": bankName, "cardCategory": cardCategory})
        else:
            cardNumber = request.POST['cardNumber']
            bankName = request.POST['bankName']
            cardCategory = request.POST['cardCategory']
            user = request.user
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
