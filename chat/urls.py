from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat_response/', views.chat_response, name='chat_response'),
]
