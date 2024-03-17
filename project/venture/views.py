from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .models import Venture


class VentureDetailView(LoginRequiredMixin, DetailView):
    model = Venture


class VentureCreateView(LoginRequiredMixin, CreateView):
    model = Venture
    fields = ['building', 'complement', 'price', 'customer']

        
class VentureUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Venture
    fields = ['building', 'complement', 'price', 'customer']

    def form_valid(self, form):
        form.instance.entrepreneur = self.request.user
        return super().form_valid(form)
    
    def test_func(self) -> bool | None:
        post = self.get_object()
        return post.entrepreneur == self.request.user


