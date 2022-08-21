from django.urls import path
from my_app import views

urlpatterns = [
    path('ping', views.Ping.as_view())
]