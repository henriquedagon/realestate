# from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms

from portal.utils.validations import PHONE_REGEX

from .models import Customer

class CustomerRegisterForm(ModelForm):
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=128)
    tax_id = forms.CharField(max_length=11)
    username = forms.CharField(max_length=32)
    email = forms.EmailField()
    phone_number = forms.CharField(validators=[PHONE_REGEX], max_length=17)


    def __init__(self, *args, **kwargs):
        super(CustomerRegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Nome'
        self.fields['last_name'].label = 'Sobrenome'
        self.fields['tax_id'].label = 'CPF'
        self.fields['username'].label = 'Apelido'
        self.fields['username'].required = False
        self.fields['email'].required = False
        self.fields['phone_number'].label = 'Telefone'
        self.fields['phone_number'].required = False

    class Meta:
        model = Customer
        fields = ['tax_id', 'first_name', 'last_name', 'username', 'email', 'phone_number']
