from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_news, name='get_news'),
]