from turtle import update
from django.db import models
from numpy import prod
from products.models import Product
from customers.models import Customer
from profiles.models import Profile
from django.utils import timezone
from .utils import generate_code
from django.shortcuts import reverse


class Position(models.Model):
    product  = models.ForeignKey(Product , on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()
    price    = models.FloatField(blank  = True)
    created  = models.DateTimeField(blank=True)
    
    ######################## Override save method #########################
    def save(self, *args, **kwargs):
        self.price  = self.product.price * self.quantity
        return super().save(args, **kwargs)
    
    
    
    def __str__(self):
        return f'Id {self.id} , product:{self.product.name} , quantity {self.quantity}'
    
class Sale(models.Model):
    transaction_id = models.CharField(max_length=12,blank=True)
    position  = models.ManyToManyField(Position)
    total_price = models.FloatField(blank  = True , null=True)
    customer    = models.ForeignKey(Customer , on_delete = models.CASCADE)
    salesman    = models.ForeignKey(Profile , on_delete = models.CASCADE)
    created  = models.DateTimeField(blank=True)
    updated  =  models.DateTimeField(auto_now  = True)   
    
    def __str__(self):
        return f"Sales for amount of ${self.total_price}"
    
    def get_absolute_url(self):
        return reverse('sales:detail',kwargs={'pk':self.pk})
        
    
    def save(self, *args, **kwargs):
        if self.transaction_id == '':
            self.transaction_id  = generate_code()
        if self.created  is None:
            self.created = timezone.now()        
        
        return super().save(args, **kwargs)
    
    def get_position(self):
        return self.position.all()
    
     
class CSV(models.Model):  
    file_name  = models.FileField(upload_to  = 'csvs')
    activated  = models.BooleanField(default = False)
    created    = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now  = True)    
    
    def __str__(self):
        return f"File Name :{self.file_name}"