"""
Views for the user api.
"""
from rest_framework import generics

from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """"""
