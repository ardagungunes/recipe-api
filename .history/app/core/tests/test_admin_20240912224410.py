"""
Tests for Django admin modifications.
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSitetests(TestCase):
    """Tests for Django admin."""

    def setUp(self):
        """Create user and client."""
        self.client = Client()
        self.admin_user = get_user_model.objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
            )
        self.client.force_login(self.admin_user)
        self.user = get_user_model.objects.create_user(
            email='user@example.com',
            password='userpass123',
            name='Test User',
        )


    def test_users_list(self):
        """Test that users are listed on page."""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assert.co