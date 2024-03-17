from django.urls import path
from . import views
from .views import (
#     VentureListView, 
    VentureDetailView,
    VentureCreateView,
#     VentureUpdateView,
#     VentureDeleteView,
#     UserVentureListView, 
)

urlpatterns = [
    # path('', views.home, name='portal-home'),
    # path('', VentureListView.as_view(), name='portal-home'),
    # path('user/<str:username>', UserVentureListView.as_view(), name='user-ventures'),
    path('<int:pk>/', VentureDetailView.as_view(), name='venture-detail'),
    path('new/', VentureCreateView.as_view(), name='venture-create'),
    # path('venture/<int:pk>/update', VentureUpdateView.as_view(), name='venture-update'),
    # path('venture/<int:pk>/delete', VentureDeleteView.as_view(), name='venture-delete'),
    # path('ventures/', views.ventures, name='ventures'),
]
