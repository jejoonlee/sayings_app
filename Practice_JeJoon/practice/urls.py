from django.urls import path
from . import views

app_name = 'practice'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('delete/<int:pk>/', views.delete, name='delete'),
  path('edit/<int:pk>/', views.edit, name='edit'),
]