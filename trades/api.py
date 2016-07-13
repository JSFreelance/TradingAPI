from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from trades.models import Trade
from trades.serializers import TradeSerializer
class TradeListAPI(ListCreateAPIView):
    queryset = Trade.objects.all().order_by('-booking_date')
    serializer_class = TradeSerializer


class TradeDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
