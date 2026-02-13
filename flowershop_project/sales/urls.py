from django.urls import path
from . import views

urlpatterns = [
    path('', views.sale_list, name='sale_list'),
    path('add/', views.sale_create, name='sale_create'),
    path('<int:pk>/delete/', views.sale_delete, name='sale_delete'),
    path('report/', views.sales_report, name='sales_report'),
]