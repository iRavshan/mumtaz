from django.urls import path
from . import views

urlpatterns = [
    path('', views.couriers_view, name='couriers'),
    path('add/', views.add_courier_view, name='add_courier'),
    path('<str:courier_key>/', views.courier_view, name='courier'),
    path('<str:courier_key>/update/', views.update_courier_view, name='update_courier'),
    path('<str:courier_key>/delete/', views.delete_courier_view, name='delete_courier'),
]