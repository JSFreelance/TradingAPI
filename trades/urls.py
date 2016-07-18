from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
import api as trades_api

router = DefaultRouter()
router.register(r'trades', trades_api.TradeViewSet)

urlpatterns = [
    url(r'1.0/', include(router.urls))
]
