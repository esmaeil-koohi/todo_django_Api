from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos_page),
]