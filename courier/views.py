from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F, Sum

from order.models import Order
from .models import Courier
from .forms import CreateCourierForm, UpdateCourierForm, LadeForm, UnladeForm


@login_required
def couriers_view(request):
    search_key = request.GET.get('search_key', '')
    if search_key:
        all_couriers = Courier.objects.filter(key=search_key)
    else:
        all_couriers = Courier.objects.all()
    return render(request, 'courier/couriers.html', {'couriers': all_couriers})


@login_required
def courier_view(request, courier_key):
    courier = get_object_or_404(Courier, key=courier_key)
    
    lade_form = LadeForm()
    unlade_form = UnladeForm()

    if request.method == 'POST':
        if 'lade_submit' in request.POST:
            lade_form = LadeForm(request.POST)
            if lade_form.is_valid():
                payload = lade_form.cleaned_data['payload']
                courier.payload += payload  # Add bottles to courier's payload
                courier.save()
                messages.success(request, f'Successfully loaded {payload} bottles onto the courier.')
                return redirect('courier', courier_key=courier.key)

        elif 'unlade_submit' in request.POST:  # Check if the unlade form was submitted
            unlade_form = UnladeForm(request.POST)
            if unlade_form.is_valid():
                payload = unlade_form.cleaned_data['payload']
                if courier.payload >= payload:
                    courier.payload -= payload  
                    courier.save()
                    messages.success(request, f'Successfully unloaded {payload} bottles from the courier.')
                else:
                    messages.error(request, 'Cannot unload more bottles than currently loaded.')
                return redirect('courier', courier_key=courier.key)

    delivered_orders = Order.objects.filter(status='delivered', courier=courier)
    delivered_bottles = delivered_orders.aggregate(
        total_bottles=Sum(F('replacement_bottles') + F('new_bottles')))['total_bottles'] or 0 
    
    assigned_orders = Order.objects.filter(courier=courier).exclude(status='delivered')
    assigned_bottles = assigned_orders.aggregate(
        total_bottles=Sum(F('replacement_bottles') + F('new_bottles')))['total_bottles'] or 0
    
    context = {
        'courier': courier,
        'delivered_orders': delivered_orders,
        'delivered_bottles': delivered_bottles,
        'assigned_orders': assigned_orders,
        'assigned_bottles': assigned_bottles,
        'lade_form': lade_form,
        'unlade_form': unlade_form
    }
    return render(request, 'courier/courier.html', context)


@login_required
def add_courier_view(request):
    if request.method == 'POST':
        form = CreateCourierForm(request.POST)
        if form.is_valid():
            new_courier = form.save(commit=True)
            return redirect('courier', courier_key=new_courier.key)
        else:
            return render(request, 'courier/add_courier.html', {'form': form})
    else:
        form = CreateCourierForm()
    return render(request, 'courier/add_courier.html', {'form': form})


@login_required
def update_courier_view(request, courier_key):
    courier = get_object_or_404(Courier, key=courier_key)
    if request.method == 'POST':
        form = UpdateCourierForm(request.POST, instance=courier)
        if form.is_valid():
            form.save()
            return redirect('courier', courier_key=courier.key)
    else:
        form = UpdateCourierForm(instance=courier)
    
    return render(request, 'courier/update_courier.html', {'form': form, 'courier': courier})


@login_required
def ban_courier_view(request, courier_key):
    courier = get_object_or_404(Courier, key=courier_key)
    courier.is_banned = True
    courier.save()
    return redirect('couriers')


@login_required
def delete_courier_view(request, courier_key):
    courier = get_object_or_404(Courier, key=courier_key)
    courier.delete()
    return redirect('couriers')