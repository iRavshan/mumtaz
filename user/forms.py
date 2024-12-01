from django import forms


class UserLoginForm(forms.Form):

    username = forms.CharField(label='Login',
                               required=True,
                               widget=forms.TextInput(attrs={'id': 'username',
                                                             'name': 'username',
                                                             'class': 'form-control',
                                                             'placeholder': 'Loginni kiriting'})) 
    
    password = forms.CharField(label='Parol',
                               required=True,
                               widget=forms.PasswordInput(attrs={'id': 'password',
                                                                 'name': 'password',
                                                                 'class': 'form-control',
                                                                 'placeholder': 'Parolni kiriting'}))