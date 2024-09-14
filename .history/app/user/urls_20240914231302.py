"""
Url mappings for the user api.
"""
from django.urls import path
from . import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view())
]
