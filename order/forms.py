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
    
    destination = forms.CharField(required=False,
                                  widget=forms.TextInput(attrs={'id': 'destination',
                                                                'name': 'destination',
                                                                'placeholder': 'Manzilni kiriting',
                                                                'class': 'form-control mb-3'}))
    
    geo_location = forms.URLField(required=False,
                                  widget=forms.URLInput(attrs={'id': 'geo_location',
                                                               'name': 'geo_location',
                                                               'placeholder': 'Geolokatsiya',
                                                               'class': 'form-control'}))
    
    delivery_pace = forms.ChoiceField(label='Yetkazish muddati',
                                      required=True,
                                      choices=[('asap', 'Tezkor'),
                                               ('later', 'Boshqa vaqtda')],
                                      widget=forms.RadioSelect(attrs={'name': 'delivery_pace',
                                                                      'class': 'form-check-input'}))
    
    preferred_delivery_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'id': 'preferred_delivery_datetime',
                                                                                        'name': 'preferred_delivery_datetime',
                                                                                        'type':'date',
                                                                                        'class': 'form-control'}))
    
    
    class Meta:
        model = Order
        fields = ['replacement_bottles', 'new_bottles', 'destination', 'geo_location']
    

class ReceiveOrderForm(forms.Form):
    courier = forms.ModelChoiceField(label='Yetkazuvchini tanlang', 
                                     queryset=Courier.objects.all(),
                                     required=True,
                                     widget=forms.Select(attrs={'name': 'courier',
                                                                      'id': 'courier',
                                                                      'class': 'form-select form-control'}))