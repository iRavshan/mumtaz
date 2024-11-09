from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders_view, name='orders'),
    path('<str:order_key>', views.order_view, name='order'),
    path('add/', views.add_order_view, name='add_order')
]