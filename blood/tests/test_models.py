from django.test import TestCase
from django.contrib.auth import get_user_model


class UserTestCase(TestCase):
    def test_create_user(self):
        """User creation"""
        email = 'normal@user.com'
        password = 'P4ssw0rd!'
        full_name = 'Normal User'

        User = get_user_model()
        user = User.objects.create_user(
            email=email,
            password=password,
            full_name=full_name,
        )

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.email, email)
        self.assertEqual(user.full_name, full_name)
        self.assertFalse(user.is_superuser)
