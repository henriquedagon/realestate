from django.urls import path
from . import views
from .views import (
    BuildingDetailView,
    BuildingCreateView,
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
    path('venture/<int:pk>/', VentureDetailView.as_view(), name='venture-detail'),
    path('venture/new/', VentureCreateView.as_view(), name='venture-create'),
    # path('venture/<int:pk>/update', VentureUpdateView.as_view(), name='venture-update'),
    # path('venture/<int:pk>/delete', VentureDeleteView.as_view(), name='venture-delete'),
    # path('ventures/', views.ventures, name='ventures'),
    path('building/<int:pk>/', BuildingDetailView.as_view(), name='building-detail'),
    path('building/new/', BuildingCreateView.as_view(), name='building-create'),
]
