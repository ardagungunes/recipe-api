"""
Tests for Django admin modifications.
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSitetests(TestCase):
    """Tests for Django admin."""