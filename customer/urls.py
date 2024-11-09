from django.urls import path
from . import views

urlpatterns = [
    path('', views.customers_view, name='customers'),
    path('add/', views.add_customer_view, name='add_customer'),
    path('<str:customer_key>/', views.customer_view, name='customer'),
    path('<str:customer_key>/update/', views.update_customer_view, name='update_customer'),
    path('<str:customer_key>/delete/', views.delete_customer_view, name='delete_customer'),
]