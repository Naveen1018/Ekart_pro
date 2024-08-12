from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import *
from .forms import *
from cart.models import Cart,Cart_items
from category.models import Category
from accounts.models import Account
from store.models import Product
from cart.views import get_cart_id
import random

# Create your views here.
def order(request, total=0, quantity=0):
    grandtotal=0
    tax=0
    try:
        cart=Cart.objects.get(cart_id=get_cart_id(request))
        cart_items=Cart_items.objects.filter(is_active=True,cart=cart)
        
        for item in cart_items:
            total+=item.product.price*item.quantity
            quantity+=item.quantity
        tax=(2*total)/100
        grandtotal+=total+tax

    except Exception :
        pass

    cart_data={
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'grandtotal':grandtotal,
        'tax':tax,
    }

    return render(request, 'place-order.html',cart_data)

def order_complete(request, total=0, quantity=0):

    grandtotal=0
    tax=0
    try:
        cart=Cart.objects.get(cart_id=get_cart_id(request))
        cart_items=Cart_items.objects.filter(is_active=True,cart=cart)
        
        for item in cart_items:
            total+=item.product.price*item.quantity
            quantity+=item.quantity
        tax=(2*total)/100
        grandtotal+=total+tax

    except Exception :
        pass

    cart_data={
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'grandtotal':grandtotal,
        'tax':tax,
    }
        
    if request.method=='POST':
        invoice = 'GRTK'+str(random.random())[2:11]
        account = Account.objects.order_by('-last_login').first()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        country = request.POST.get('country')
        state = request.POST.get('state')
        street = request.POST.get('street')
        building = request.POST.get('building')
        house = request.POST.get('house')
        postal = request.POST.get('postal')

        cardno = request.POST.get('cardno')
        expiry = request.POST.get('expiry')
        cvv = request.POST.get('cvv')

        amount = grandtotal
        card = str(cardno)[-4:]

        feetotal = grandtotal+40

        data = order_model(invoice=invoice, account=account, first_name=first_name, last_name=last_name, phone=phone, email=email, country=country, state=state, street=street, building=building, house=house, postal=postal, cardno=cardno, expiry=expiry, cvv=cvv, amount=amount, card=card, feetotal=feetotal)
        data.save()

        product = None
        for i in cart_items:
            product = i.product.product_name
            price = i.product.price
            invoice = order_model.objects.order_by('-orderdate').first()
            image = i.product.images.url
            items = order_items(inv=invoice,product=product, image=image, price=price)
            items.save()

    return render(request, 'order_complete.html',cart_data)

def dashboard(request):
    return render(request, 'dashboard.html')

def product_detail(request, category_slug, product_slug):
    product_=None
    try:
        product_=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        print(e)
    
    return render(request,'product-detail.html',{'product':product_,})
