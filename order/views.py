from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Order
from .forms import CreateOrderForm, ReceiveOrderForm


@login_required
def orders_view(request):
    search_key = request.GET.get('search_key', '')
    if search_key:
        all_orders = Order.objects.filter(key=search_key)
    else:
        all_orders = Order.objects.all()
    return render(request, 'order/orders.html', {'orders': all_orders})


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