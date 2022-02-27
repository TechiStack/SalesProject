from sqlite3 import Date
from django import forms

Chart_Choice = (
    ('#1' , 'Bar chart'),
    ('#2' , 'Pie chart'),
    ('#3' , 'Line chart')
)
class SalesSearchForm(forms.Form):
    date_from =forms.DateField(widget=forms.DateInput(attrs={'type':'date'}) ,required=False)
    date_to   = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}) ,required=False)
    chart_type = forms.ChoiceField(choices=Chart_Choice)



    
    
    