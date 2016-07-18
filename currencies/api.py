from rest_framework.generics import ListCreateAPIView
from currencies.models import Currency
from currencies.serializers import CurrencySerializer


class CurrencyListAPI(ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
