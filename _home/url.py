from django.urls import path

from . import views

app_name = '_home'

urlpatterns = [
    path('', views._home, name='_home'),
]
# © 2021 GitHub, Inc.
