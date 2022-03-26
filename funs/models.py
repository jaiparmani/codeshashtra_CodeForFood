from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)


class CardType(models.Model):
    bank = models.CharField(max_length=20)
    card_type = models.CharField(max_length=20)  # Debit or credit gold


class Card(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=20)
    card_type = models.ForeignKey(CardType, on_delete=models.CASCADE)
    # card_ name = models.CharField(max_length=20)
    # card_expiry = models.CharField(max_length=20)
    # card_cvv = models.CharField(max_length=20)


class OfferCategory(models.Model):
    category = models.CharField(max_length=20)


class OfferDetails(models.Model):
    minOrder = models.IntegerField(null=True)
    maxOrder = models.IntegerField(null=True)
    offerPercentage = models.IntegerField(null=True)
    offerValidUpto = models.DateField(null=True)


class Offer(models.Model):
    onCard = models.ForeignKey(Card, on_delete=models.CASCADE)
    offerTitle = models.CharField(max_length=20)
    offerSource = models.CharField(max_length=20)
    offerDescription = models.CharField(max_length=20)
    offerImage = models.CharField(max_length=20)
    offerLink = models.CharField(max_length=100)
    offerPrice = models.FloatField()
    offerCategory = models.ForeignKey(OfferCategory, on_delete=models.CASCADE)

    offerDetails = models.ForeignKey(OfferDetails, on_delete=models.CASCADE)
