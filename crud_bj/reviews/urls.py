from django.urls import path
from . import views


app_name = "reviews"
urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("edit/<int:pk>", views.edit, name="edit"),
    path("detail/<int:pk>", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("update/<int:pk>", views.update, name="update"),
]
