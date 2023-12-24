# gender/urls.py
from django.urls import path
from .views import home, male, female, message

urlpatterns = [
    path('', home, name='home'),
    path('male/', male, name='male'),
    path('female/', female, name='female'),
    path('message/<str:submitted_behaviors>/', message, name='message'),
]
