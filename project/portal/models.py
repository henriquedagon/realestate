from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from portal.utils.states import STATE_CODES
from portal.utils.validations import PHONE_REGEX

import phonenumbers

# from venture.models import Venture


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Personal info
    username = models.CharField(max_length=32, null=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=128)
    tax_id = models.CharField(max_length=11)
    # Contacts
    email = models.EmailField(default=None, null=True)
    phone_number = models.CharField(validators=[PHONE_REGEX], max_length=17, null=True)
    # Residential info
    street_name = models.CharField(max_length=256, null=True)
    street_number = models.IntegerField(null=True)
    neighborhood = models.CharField(max_length=64, null=True)
    city = models.CharField(max_length=64, null=True)
    state = models.CharField(max_length=2, choices=STATE_CODES, null=True)
    # User
    entrepreneur = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse('customer-detail', kwargs={'pk': self.pk})

    @property
    def full_name(self):
        "Returns the person's full name."
        return f"{self.first_name} {self.last_name}"

    @property
    def formatted_phone_number(self, country="BR"):
        if (self.phone_number):
            return phonenumbers.format_number(
                phonenumbers.parse(self.phone_number, country), 
                phonenumbers.PhoneNumberFormat.NATIONAL
            )
        return None