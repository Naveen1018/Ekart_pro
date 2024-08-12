from .models import order_model, order_items
from accounts.models import Account
from store.models import Product

def order_details(request):
    details = order_model.objects.order_by('-orderdate') # '-orderdate' used for desc order
    return dict(order_details=details)

def orderhistory(request):
    details = order_items.objects.all()
    return dict(orderhistory=details)

def order_invoice(request):
    details = order_model.objects.order_by('-orderdate').first()
    return dict(order_invoice=details)

def order_count(request):
    email = Account.objects.order_by('-last_login').first()
    details = order_model.objects.filter(account = email)
    count = details.count()
    return dict(order_count=count)

def category(request):
    p = Product.objects.filter(is_avaiable=True)
    return dict(category=p)