from django.db import models

# Create your models here.
class order_model(models.Model):
    invoice = models.CharField(max_length=20, unique=True, null=True)
    account = models.EmailField(null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()

    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    street =  models.CharField(max_length=100)
    building =  models.CharField(max_length=100)
    house =  models.CharField(max_length=100)
    postal = models.IntegerField()

    cardno = models.IntegerField()
    expiry = models.CharField(max_length=10)
    cvv = models.IntegerField()

    amount = models.IntegerField(null=True)
    card = models.CharField(max_length=4,null=True)
    feetotal = models.IntegerField(null=True)
    orderdate = models.DateTimeField(auto_now=True)

class order_items(models.Model):
    inv = models.ForeignKey(order_model,on_delete=models.CASCADE, null=True)
    product = models.CharField(max_length=225)
    price = models.IntegerField(null=True)
    image = models.ImageField(upload_to='photos/orders', blank=True)