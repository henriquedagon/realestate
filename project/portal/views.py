from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.db.models import Count
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
# from project import venture

from venture.models import Building, Venture

from .models import Customer


def home(request):
    # Users customers
    customers = [customer for customer in 
        Customer.objects.filter(entrepreneur=request.user)]
    # Users ventures
    ventures = Venture.objects.filter(
        customer__in=customers).values('building').annotate(total=Count('building'))
    # Users buildings ventures' count
    buildings_count = [{
        'building': Building.objects.get(pk=venture['building']), 
        'total': venture['total']} 
    for venture in ventures]

    context = {
        'customers': customers,
        'buildings': [building for building in Building.objects.all()],
        'buildings_count': buildings_count,
        'user': request.user,
    }
    return render(request, 'portal/home.html', context=context)


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer

def get_context_data(self, **kwargs):
    context = super(CustomerDetailView, self).get_context_data(**kwargs)
    context['ventures'] = Venture.objects.filter(customer=self.object)
    return context


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ['name', 'tax_id']

    def form_valid(self, form):
        form.instance.entrepreneur = self.request.user
        return super().form_valid(form)

