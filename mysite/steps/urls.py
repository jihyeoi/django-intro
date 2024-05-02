from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('start/', views.list_steps, name='list_steps'),
]