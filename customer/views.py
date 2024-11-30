from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from customer.forms import CreateCustomerForm, UpdateCustomerForm
from order.models import Order
from order.forms import CreateOrderForm
from .models import Customer


@login_required
def customers_view(request):
    
    phone_number = request.GET.get('phone_number', '')
    first_name = request.GET.get('first_name', '')
    last_name = request.GET.get('last_name', '')
    address = request.GET.get('address', '')
    
    all_customers = Customer.objects.all()
    
    if phone_number or first_name or last_name or address:
        if phone_number:
            all_customers = all_customers.filter(phone_number=phone_number)
        if first_name:
            first_name = first_name.lower().capitalize()
            all_customers = all_customers.filter(first_name=first_name)  
        if last_name:
            last_name = last_name.lower().capitalize()
            all_customers = all_customers.filter(last_name=last_name)
        if address:
            all_customers = all_customers.filter(address__icontains=address)     
        
    return render(request, 'customer/customers.html', {'customers': all_customers})


@login_required
def customer_view(request, customer_key):
    get_customer = get_object_or_404(Customer, key=customer_key)
    orders = Order.objects.filter(customer=get_customer)
    
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            replacement_bottles = form.cleaned_data['replacement_bottles']
            new_bottles = form.cleaned_data['new_bottles']
            new_order = Order(replacement_bottles=replacement_bottles, new_bottles=new_bottles, customer=get_customer)
            new_order.save()
            return redirect('order', order_key=new_order.key)
    else:
        form = CreateOrderForm()
    
    context = {
        'customer': get_customer,
        'orders': orders,
        'form': form
    }
    
    return render(request, 'customer/customer.html', context)


@login_required
def add_customer_view(request):
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            new_customer = form.save(commit=True)
            return redirect('customer', customer_key=new_customer.key)
        else:
            return render(request, 'customer/add_customer.html', {'form': form})
    else:
        form = CreateCustomerForm()
    return render(request, 'customer/add_customer.html', {'form': form})


@login_required
def update_customer_view(request, customer_key):
    customer = get_object_or_404(Customer, key=customer_key)
    if request.method == 'POST':
        form = UpdateCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer', customer_key=customer.key)
    else:
        form = UpdateCustomerForm(instance=customer)
    
    return render(request, 'customer/update_customer.html', {'form': form, 'customer': customer})


@login_required
def delete_customer_view(request, courier_key):
    customer = get_object_or_404(Customer, key=courier_key)
    customer.delete()
    return redirect('customers')
    