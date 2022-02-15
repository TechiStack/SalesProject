from django.contrib import admin
from .models import *


#Model defined to represent admin view
admin.site.register(Position)
admin.site.register(Sale)
admin.site.register(CSV)


