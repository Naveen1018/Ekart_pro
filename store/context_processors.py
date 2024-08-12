from .models import Product

def pricerange(request):
    pricerangedata = Product.objects.all().order_by('price')
    return dict(pricerange=pricerangedata)