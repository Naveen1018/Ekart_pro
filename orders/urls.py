from django.urls import path
from .views import *
from store.views import product_details
app_name = 'orders'

urlpatterns = [
    path('order/', order, name='order'),
    path('order_complete/', order_complete, name='order_complete'),
    path('dashboard/', dashboard, name='dashboard'),
    path('category/<slug:category_slug>/<slug:product_slug>',product_details,name='product_details'),
]