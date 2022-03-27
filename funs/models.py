from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __unicode__(self):
        return self.username


class CardType(models.Model):
    bank = models.CharField(max_length=20)
    card_type = models.CharField(max_length=20)  # Debit or credit gold

    def __str__(self):
        return self.card_type + " " + self.bank


class Card(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=20)
    card_type = models.ForeignKey(CardType, on_delete=models.CASCADE)
    # card_ name = models.CharField(max_length=20)
    # card_expiry = models.CharField(max_length=20)
    # card_cvv = models.CharField(max_length=20)

    def __str__(self):
        return self.card_number


class OfferCategory(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class OfferDetails(models.Model):
    minOrder = models.IntegerField(null=True)
    maxOrder = models.IntegerField(null=True)
    offerPercentage = models.IntegerField(null=True)
    offerValidUpto = models.DateField(null=True)

    def __str__(self):
        return self.offerPercentage


class Offer(models.Model):
    onCard = models.ForeignKey(CardType, on_delete=models.CASCADE)
    offerTitle = models.CharField(max_length=20)
    offerSource = models.CharField(max_length=20, blank=True)
    offerID = models.IntegerField()
    offerDescription = models.CharField(max_length=100  , blank=True)
    offerImage = models.CharField(max_length=900000   , null=True, blank=True)
    offerLink = models.CharField(max_length=100, null=True, blank=True)
    offerPrice = models.FloatField(null=True, blank=True)
    offerCategory = models.ForeignKey(OfferCategory, on_delete=models.CASCADE)

    # offerDetails = models.ForeignKey(OfferDetails, on_delete=models.CASCADE)
    minOrder = models.IntegerField(null=True, blank=True)
    maxOrder = models.IntegerField(null=True, blank=True)
    offerPercentage = models.IntegerField(null=True, blank=True)
    offerValidUpto = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.offerTitle
