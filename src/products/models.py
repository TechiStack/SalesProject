from pyexpat import model
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120)
    image =  models.ImageField(default='no_picture.png')
    price = models.FloatField(help_text='in US dollars $')
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}--{self.created.strftime('%Y-%m-%d')}"
    
