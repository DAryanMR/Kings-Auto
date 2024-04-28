from django import forms
from .models import Service, Stuff


class SaleForm(forms.Form):
    sale_date = forms.DateField()
    customer_name = forms.CharField(max_length=100)
    car_name = forms.CharField(max_length=100)
    car_reg = forms.CharField(max_length=20)
    chassis_no = forms.CharField(max_length=50)
    service = forms.ModelChoiceField(queryset=Service.objects.all())
    qty = forms.IntegerField(initial=1)
    stuff = forms.ModelChoiceField(queryset=Stuff.objects.all())
