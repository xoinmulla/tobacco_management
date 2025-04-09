from django.urls import path
from . import views  # Import views from the same directory
from .views import product_list,contact,contact_success

urlpatterns = [
    path('', views.home, name='home'),  # Example route
    path('products/', views.product_list, name='products'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.customer_register, name='register'),

]
