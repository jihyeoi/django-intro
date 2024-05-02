from django.urls import path
from . import views

urlpatterns = [
    path('testimonials/', views.show_testimonials, name='show_testimonials'),
    path('testimonials/new', views.post_new, name='post_new'),
]