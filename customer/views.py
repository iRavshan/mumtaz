from django.shortcuts import render, get_object_or_404, redirect
from customer.forms import CreateCustomerForm, UpdateCustomerForm
from order.models import Order
from order.forms import CreateOrderForm
from .models import Customer


def customers_view(request):
    search_key = request.GET.get('search_key', '')
    if search_key:
        all_customers = Customer.objects.filter(phone_number=search_key)
    else:
        all_customers = Customer.objects.all()
    return render(request, 'customer/customers.html', {'customers': all_customers})


def customer_view(request, customer_key):
    get_customer = get_object_or_404(Customer, key=customer_key)
    orders = Order.objects.filter(customer=get_customer)
    form = CreateOrderForm()
    context = {
        'customer': get_customer,
        'orders': orders,
        'form': form
    }
    return render(request, 'customer/customer.html', context)


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

def delete_customer_view(request, courier_key):
    customer = get_object_or_404(Customer, key=courier_key)
    customer.delete()
    return redirect('customers')
    