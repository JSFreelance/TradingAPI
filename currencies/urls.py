from django.conf.urls import url
import api as currencies_api

urlpatterns = [
    # Currencies API
    url(r'currencies/', currencies_api.CurrencyListAPI.as_view(),
        name='currency_list_api')
]
