from rest_framework.viewsets import ModelViewSet
from trades.models import Trade
from trades.serializers import TradeSerializer


class TradeViewSet(ModelViewSet):
    queryset = Trade.objects.all().order_by('-booking_date')
    serializer_class = TradeSerializer

