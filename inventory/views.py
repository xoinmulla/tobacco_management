from django.shortcuts import render,redirect
from .models import Product  # Ensure Product model exists
from .forms import ContactForm

def product_list(request):
    products = [
        {'name': 'Cigarettes', 'quantity': 50, 'price': 10},
        {'name': 'Chewing Tobacco', 'quantity': 30, 'price': 5},
        {'name': 'Cigars', 'quantity': 20, 'price': 15},
    ]
    return render(request, 'inventory/products.html', {'products': products})

def home(request):
    return render(request, 'inventory/home.html')  # Ensure template exists

def contact(request):
    return render(request, 'inventory/contact.html')

def contact_success(request):
    return render(request, 'contact_success.html') 

    path('register/', views.customer_register, name='register'),
from django.shortcuts import render, redirect
from .models import Product
from .forms import ContactForm, CustomerForm

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'inventory/contact.html', {'form': form})


def customer_register(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm()
    return render(request, 'inventory/customer_register.html', {'form': form})

