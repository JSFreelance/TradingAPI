from __future__ import unicode_literals
from django.db import models
from currencies.models import Currency
# Create your models here.
class Trade(models.Model):

    sell_currency = models.ForeignKey(Currency, related_name='sell_currency')
    sell_amount = models.FloatField(null=False, blank=False)
    buy_currency = models.ForeignKey(Currency)
    buy_amount = models.FloatField(null=False, blank=False)
    rate = models.FloatField(null=False, blank=False)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.sell_currency) + '->' + str(self.rate) + '->' + str(self.buy_currency)
