from django.urls import path
from . import views

# app_name = 'accounts'
urlpatterns = [
    path('', views.show_home, name='show_home'),
]
