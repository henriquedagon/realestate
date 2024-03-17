from django.db import models

from portal.models import Customer
from django.urls import reverse


class Building(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.name


    def __str__(self):
        return self.name


class Venture(models.Model):
    id = models.AutoField(primary_key=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='Edifício')
    complement = models.CharField(max_length=32, verbose_name='Complemento')
    price = models.FloatField(default=0, verbose_name='Preço')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Cliente')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.building.name} {self.complement}"


    def get_absolute_url(self):
        return reverse('venture-detail', kwargs={'pk': self.pk})
