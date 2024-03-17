from django.contrib import admin
from .models import (
    Building,
    Venture
)

admin.site.register(Building)
admin.site.register(Venture)