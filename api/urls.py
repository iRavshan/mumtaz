from django.urls import include, path
from rest_framework import routers

from api.views import CourierViewSet, CustomerViewSet, OrderViewSet

router = routers.DefaultRouter()

router.register(r'couriers', CourierViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]