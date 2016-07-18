from django.conf.urls import url
import api as trades_api

urlpatterns = [
    # Trades API urls
    url(r'trades/$', trades_api.TradeListAPI.as_view(), name='trade_list_api'),
    url(r'trades/(?P<pk>[0-9]+)$',
        trades_api.TradeDetailAPI.as_view(), name='trade_detail_api')
]
