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