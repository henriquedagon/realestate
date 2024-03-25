from django.forms import ModelForm

from .models import Venture, Building

class BuildingCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BuildingCreationForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Nome'
        self.fields['street_name'].label = 'Rua'
        self.fields['street_number'].label = 'Número'
        self.fields['neighborhood'].label = 'Bairro'
        self.fields['city'].label = 'Cidade'
        self.fields['state'].label = 'Estado'

    class Meta:
        model = Building
        fields = ['name', 'street_name', 'street_number', 'neighborhood', 'city', 'state']


class VentureCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(VentureCreationForm, self).__init__(*args, **kwargs)
        self.fields['building'].label = 'Empreendimento'
        self.fields['complement'].label = 'Complemento'
        self.fields['price'].label = 'Preço'
        self.fields['customer'].label = 'Cliente'

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


