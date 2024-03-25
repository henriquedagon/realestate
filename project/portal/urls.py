from django.urls import path
from . import views
from .views import (
#     CustomerListView, 
    CustomerDetailView,
    CustomerCreateView,
#     CustomerUpdateView,
#     CustomerDeleteView,
#     UserCustomerListView, 
)

urlpatterns = [
    # path('media/favicon.jpg', name='favicon')
    path('', views.home, name='portal-home'),
    # path('', CustomerListView.as_view(), name='portal-home'),
    # path('user/<str:username>', UserCustomerListView.as_view(), name='user-customers'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('customer/new/', CustomerCreateView.as_view(), name='customer-create'),
    # path('customer/<int:pk>/update', CustomerUpdateView.as_view(), name='customer-update'),
    # path('customer/<int:pk>/delete', CustomerDeleteView.as_view(), name='customer-delete'),
    # path('customers/', views.customers, name='portal-customers'),
]
