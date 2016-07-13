from django.conf.urls import url
from django.contrib import admin
from trades import api as trades_api
from currencies import api as currencies_api
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Trades API urls
    url(r'^api/1.0/trades/$', trades_api.TradeListAPI.as_view(), name='trade_list_api'),
    url(r'^api/1.0/trades/(?P<pk>[0-9]+)$', trades_api.TradeDetailAPI.as_view(), name='trade_detail_api'),
    #Currency API urls
    url(r'^api/1.0/currencies/', currencies_api.CurrencyListAPI.as_view(), name='currency_list_api')
]
