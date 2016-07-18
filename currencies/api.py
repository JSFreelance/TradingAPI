from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from currencies.models import Currency
from currencies.serializers import CurrencySerializer


class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

# class CurrencyListAPI(ListCreateAPIView):
#     queryset = Currency.objects.all()
#     serializer_class = CurrencySerializer
