from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
import api as currencies_api

router = DefaultRouter()
router.register(r'currencies', currencies_api.CurrencyViewSet)

urlpatterns = [
    url(r'1.0/', include(router.urls))
]
