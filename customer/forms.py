from django import forms
from customer.models import Customer


class CreateCustomerForm(forms.ModelForm):
    
    first_name = forms.CharField(label='Ismi',
                                 max_length=50, 
                                 required=True,
                                 widget=forms.TextInput(attrs={'id': 'first_name',
                                                               'class': 'form-control',
                                                               'placeholder': 'Ismni kiriting'}))
    last_name = forms.CharField(label='Familiyasi (ixtiyoriy)',
                                 max_length=50, 
                                 required=False,
                                 widget=forms.TextInput(attrs={'id': 'last_name',
                                                               'class': 'form-control',
                                                               'placeholder': 'Familiya'}))
    
    phone_number = forms.CharField(label='Telefon raqam', 
                                   max_length=20, 
                                   required=True,
                                   widget=forms.TextInput(attrs={'id': 'phone_number',
                                                                 'class': 'form-control',
                                                                 'data-mask': '00 000-00-00',
                                                                 'placeholder': '__ ___-__-__'}))
    
    address = forms.CharField(label='Doimiy manzil',
                               max_length=200, 
                               required=True,
                               widget=forms.TextInput(attrs={'id': 'location',
                                                             'class': 'form-control',
                                                             'placeholder': 'Doimiy manzilni kiriting'}))
    
    geo_location = forms.URLField(label='Geolokatsiya',
                                  required=False,
                                  widget=forms.TextInput(attrs={'id': 'geo_location',
                                                                'class': 'form-control',
                                                                'placeholder': 'Doimiy manzil uchun geolokatsiyani kiriting'}))
    
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'geo_location']
        
    
    
class UpdateCustomerForm(CreateCustomerForm):
    class Meta:
        model = Customer
        fields = ['phone_number', 'first_name', 'last_name', 'address', 'geo_location']