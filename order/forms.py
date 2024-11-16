from django import forms
from .models import Order
from courier.models import Courier

class CreateOrderForm(forms.ModelForm):
    
    replacement_bottles = forms.IntegerField(label='Almashishga',
                                            required=True,
                                            widget=forms.NumberInput(attrs={'id': 'replacement_bottles',
                                                                            'name': 'replacement_bottles',
                                                                            'class': 'form-control',
                                                                            'min': '0'}))
    new_bottles = forms.IntegerField(label="Qo'shimcha",
                                     required=True,
                                     widget=forms.NumberInput(attrs={'id': 'new_bottles',
                                                                     'name': 'new_bottles',
                                                                     'class': 'form-control',
                                                                     'min': '0'})) 
    
    class Meta:
        model = Order
        fields = ['replacement_bottles', 'new_bottles']
    

class ReceiveOrderForm(forms.Form):
    courier = forms.ModelChoiceField(label='Yetkazuvchini tanlang', 
                                     queryset=Courier.objects.all(),
                                     required=True,
                                     widget=forms.Select(attrs={'name': 'courier',
                                                                'id': 'courier',
                                                                'class': 'form-select form-control'}))