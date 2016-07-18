from django.conf.urls import url, include
from django.contrib import admin

endpoints = {
    "api": "^api/1.0/"
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Trades API urls
    url(r''.join(endpoints.get('api')),  include('trades.urls')),
    # Currency API urls
    url(r''.join(endpoints.get('api')), include('currencies.urls'))
]
