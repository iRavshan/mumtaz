from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from customer.models import Customer
from user.models import CustomUser
from courier.models import Courier
from order.models import Order

@login_required
def home(request):
    new_orders = Order.objects.filter(status='new')
    customers = Customer.objects.count()
    couriers = Courier.objects.count()
    employees = CustomUser.objects.count()
    delivered_orders = Order.objects.filter(status='delivered', delivered_at__date=timezone.now().date()).count()
    delivering_orders = Order.objects.filter(status='delivering').count()
    on_road_couriers = Order.objects.filter(status='delivering').values('courier').distinct().count()
    
    context = {
        'customers': customers,
        'couriers': couriers,
        'employees': employees,
        'new_orders': new_orders,
        'delivered_orders': delivered_orders,
        'delivering_orders': delivering_orders,
        'on_road_couriers': on_road_couriers
    }
    
    return render(request, 'home/home.html', context)


def robots_txt(request):
    return render(request, 'robots.txt', content_type='text/plain')