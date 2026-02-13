from django.urls import path
from . import views

urlpatterns = [
    path('flowers/', views.flower_list, name='flower_list'),
    path('flowers/add/', views.flower_create, name='flower_create'),
    path('flowers/<int:pk>/edit/', views.flower_update, name='flower_update'),
    path('flowers/<int:pk>/delete/', views.flower_delete, name='flower_delete'),
    
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/add/', views.supplier_create, name='supplier_create'),
    path('suppliers/<int:pk>/edit/', views.supplier_update, name='supplier_update'),
    path('suppliers/<int:pk>/delete/', views.supplier_delete, name='supplier_delete'),
]