from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Sale
from .forms import SalesSearchForm
import pandas as pd
# Create your views here.


def home_view(request):
    form  = SalesSearchForm(request.POST or None)
    
    if request.method  == 'POST':
        searchResult = ''
        
        date_from  =  request.POST.get('date_from')
        date_to  =  request.POST.get('date_to')
        chart_type  =  request.POST.get('chart_type')
        
        qs  =  Sale.objects.filter(
                                    created__date__lte=date_from ,created__date__gte = date_to
                  
                  
                                   )
        # qs = Sale.objects.all()
        df1  = pd.DataFrame(qs.values())
        print(df1)
        
        if (len(qs) > 0):
            searchResult = 'Search Exist'
        else:
            searchResult  = 'Not Result exist'
        
        # print(f"Date From {date_from}")
        # print(f"Date to {date_to}")
        # print(f"chart_type  {chart_type}")
       
    
    context = {
        'hello' : 'Hellow Forms!', 
        'form' : form,
        'searchResult':searchResult
    }
    return render(request, 'sales/home.html',context)


class SalesListView(ListView):
    
    model  = Sale
    template_name = 'sales/main.html'
    
class SaleDetailView(DetailView):
    model  = Sale
    template_name = 'sales/detail.html'
        


def sale_list_view(request):
    qs  = Sale.objects.all()
    return render(request,'sales/main.html',{'object_list': qs})

def sale_list_detail(request,kwargs):
    pk = kwargs.get('pk')
    obj = Sale.objects.get(pk = pk)
    
        