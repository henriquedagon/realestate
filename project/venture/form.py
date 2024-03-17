from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Venture


class VentureRegisterForm(UserCreationForm):
    # first_name = forms.CharField(max_length=50)
    # last_name = forms.CharField(max_length=50)
    # email = forms.EmailField()

    class Meta:
        model = Venture
        fields = ['building', 'complement', 'price', 'customer']

# class UserUpdateForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     email = forms.EmailField()

#     def __init__(self, *args, **kwargs):
#         super(UserUpdateForm, self).__init__(*args, **kwargs)
#         self.fields['username'].label = 'Usuário'
#         self.fields['first_name'].label = 'Nome'
#         self.fields['last_name'].label = 'Sobrenome'

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name']



# class VentureCreationForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(VentureCreationForm, self).__init__(*args, **kwargs)
#         self.fields['building'].label = 'Empreendimento'
#         self.fields['complement'].label = 'Complemento'
#         self.fields['price'].label = 'Preço'
#         self.fields['customer'].label = 'Cliente'

#     class Meta:
#         model = Venture
#         fields = ['building', 'complement', 'price', 'customer']