from django.test import TestCase


class RegisterTestCase(TestCase):
    def test_home_view(self):
        """Home page"""
        response = self.client.get('localhost:8000')
        self.assertEqual(response.status_code, 200)