"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """Tests models."""

    def test_create_user_with_email_successful(self,):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpas123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        

