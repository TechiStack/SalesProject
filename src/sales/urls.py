from django.urls import URLPattern, path
from .views import (
     home_view,
     SalesListView,
     SaleDetailView
     
)


app_name  = 'sales'

urlpatterns = [
    path('',home_view, name='home'),
    path('sales/',SalesListView.as_view(), name='list'),
    path('sale/<pk>/',SaleDetailView .as_view(), name='detail')
]