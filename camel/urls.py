from django.urls import path
from . import views

app_name = 'camel'

urlpatterns = [
    path('', views.home, name='home'),
]