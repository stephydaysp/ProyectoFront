from django.urls import path
from . import views

app_name = 'Pfront'

urlpatterns = [
    path('', views.home, name='home'),
]

