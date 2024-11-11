from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, robots_txt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('orders/', include('order.urls')),
    path('customers/', include('customer.urls')),
    path('couriers/', include('courier.urls')),
    path('robots.txt', robots_txt, name='robots_txt'),
    
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)