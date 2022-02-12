from distutils.command.upload import upload
from turtle import mode
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to = 'customers' , default = 'no_picture.png')
    
    
    def __str__(self):
        return str(self.name)


