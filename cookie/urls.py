from django.urls import path

from . import views

app_name = 'cookie'

urlpatterns = [
    path('', views.cookie, name='cookie'),
]