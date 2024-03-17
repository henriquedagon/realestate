from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# from venture.models import Venture


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    tax_id = models.CharField(max_length=11, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # personal_data = models.ForeignKey(PersonalData, null=True, on_delete=models.SET_NULL)
    entrepreneur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('customer-detail', kwargs={'pk': self.pk})

    class PersonalData(models.Model):
        name = models.CharField(max_length=128)
        tax_id = models.CharField(max_length=11, default='')


