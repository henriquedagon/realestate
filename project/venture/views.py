from django.db.models import Count
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
# from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from portal.models import Customer

from venture.form import VentureCreationForm, BuildingCreationForm

from .models import Venture, Building


class BuildingCreateView(LoginRequiredMixin, CreateView):
    model = Building
    form_class = BuildingCreationForm


class BuildingDetailView(LoginRequiredMixin, DetailView):
    model = Building

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Users customers
        customers = [customer for customer in 
            Customer.objects.filter(entrepreneur=self.request.user)]
        ventures = context['object'].venture_set.filter(customer__in=customers)
        customers_count = ventures.values('customer').annotate(total=Count('customer'))
        customers_count = [{'customer':Customer.objects.get(pk=customer['customer']), 'total':customer['total']} for customer in customers_count]
        context["customers_count"] = customers_count
        return context

class VentureDetailView(LoginRequiredMixin, DetailView):
    model = Venture


class VentureCreateView(LoginRequiredMixin, CreateView):
    model = Venture
    form_class = VentureCreationForm
    # fields = ['building', 'complement', 'price', 'customer']

        
# class VentureUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Venture
#     fields = ['building', 'complement', 'price', 'customer']

#     def form_valid(self, form):
#         form.instance.entrepreneur = self.request.user
#         return super().form_valid(form)
    
#     def test_func(self) -> bool | None:
#         post = self.get_object()
#         return post.entrepreneur == self.request.user


