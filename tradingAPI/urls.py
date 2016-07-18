from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Trades API urls
    url(r'', include('trades.urls')),
    # Currency API urls
    url(r'', include('currencies.urls'))
]
