from django import forms
from .models import Courier

class CreateCourierForm(forms.ModelForm):
    
    first_name = forms.CharField(label='Ismi',
                                 max_length=50, 
                                 required=True,
                                 widget=forms.TextInput(attrs={'id': 'first_name',
                                                               'name': 'first_name',
                                                               'class': 'form-control',
                                                               'placeholder': 'Ismni kiriting'}))
    last_name = forms.CharField(label='Familiya',
                                max_length=50, 
                                required=True,
                                widget=forms.TextInput(attrs={'id': 'last_name',
                                                              'name': 'last_name',
                                                              'class': 'form-control',
                                                              'placeholder': 'Familiyani kiriting'}))
    
    class Meta:
        model = Courier
        fields = ['first_name', 'last_name']
        

class UpdateCourierForm(CreateCourierForm):
    class Meta:
        model = Courier
        fields = ['first_name', 'last_name']
        

class LadeForm(forms.Form):
    
    payload = forms.IntegerField(required=True,
                                 widget=forms.TextInput(attrs={'id': 'payload',
                                                               'name': 'payload',
                                                               'class': 'form-control mb-3',
                                                               'type': 'number',
                                                               'min': '1',
                                                               'placeholder': 'Suv idishlari sonini kiriting'}))
    
class UnladeForm(LadeForm):
    pass    