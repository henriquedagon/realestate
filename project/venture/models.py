from django.db import models

from portal.models import Customer
from django.urls import reverse

from portal.utils.states import STATE_CODES


class Building(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    street_name = models.CharField(max_length=256, null=True)
    street_number = models.IntegerField(null=True)
    neighborhood = models.CharField(max_length=64, null=True)
    city = models.CharField(max_length=64, null=True)
    state = models.CharField(max_length=2, choices=STATE_CODES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def address(self):
        "Returns the person's full name."
        return f"{self.street_name} {self.street_number}"

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('building-detail', kwargs={'pk': self.pk})


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
