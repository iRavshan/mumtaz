from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Order
from .forms import CreateOrderForm, ReceiveOrderForm


@login_required
def orders_view(request):
    search_key = request.GET.get('search_key', '')
    
    if search_key:
        searched_orders = Order.objects.filter(key=search_key)
        context = {'searched_orders': searched_orders}
    else:
        today = now().date()
        start_of_week = today - timedelta(days=today.weekday())  # Monday of the current week
        start_of_month = today.replace(day=1)  # First day of the current month

        orders_today = Order.objects.filter(created_at__date=today)
        orders_this_week = Order.objects.filter(created_at__date__gte=start_of_week)
        orders_this_month = Order.objects.filter(created_at__date__gte=start_of_month)
        
        context = {
            'orders_today': orders_today,
            'orders_this_week': orders_this_week,
            'orders_this_month': orders_this_month
        }
    
    return render(request, 'order/orders.html', context)


@login_required
def order_view(request, order_key):
    order = Order.objects.get(key=order_key)
    receive_form = ReceiveOrderForm()
    
    if request.method == 'POST':
        receive_form = ReceiveOrderForm(request.POST)
        if receive_form.is_valid():
            courier = receive_form.cleaned_data['courier']
            order.courier = courier
            order.received_by = request.user
            order.received_at = datetime.now()
            order.status = 'received'
            order.save()     

    context = {
        'order': order,
        'receive_form': receive_form
    }

    return render(request, 'order/order.html', context)


@login_required
def add_order_view(request):
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            new_order = form.save(commit=True)
            return redirect('order', order_key=new_order.key)
        else:
            return render(request, 'order/add_order.html', {'form': form})
    else:
        form = CreateOrderForm()
    return render(request, 'order/add_order.html', {'form': form})