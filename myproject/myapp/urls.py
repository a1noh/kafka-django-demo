from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('send/', views.send_message, name='send_message'),
    path('receive_msg/', views.receive_message, name='receive_message'),
]