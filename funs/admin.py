from django.contrib import admin
from .models import Users, CardType, Card, OfferCategory, OfferDetails, Offer
# Register your models here.
admin.site.register(Users)
admin.site.register(CardType)
admin.site.register(Card)
admin.site.register(OfferCategory)
admin.site.register(OfferDetails)
admin.site.register(Offer)
