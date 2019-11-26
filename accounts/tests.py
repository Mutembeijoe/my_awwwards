from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import CustomUser

# Create your tests here.

class TestUser(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = "dummy",
            email = "dummy@test.com",
            password = 'secret'
        )

    def test_get_absolute_url(self):
        self.assertEqual(self.user.get_absolute_url(), '/accounts/user/1/')

    def test_is_instance(self):
        self.assertIsInstance(self.user, get_user_model())

    def test_user_is_saved(self):
        test_user = get_user_model().objects.create_user(
            username = "test",
            email = "dummy@test.com",
            password = 'secret'
        )
        test_user.save()
        my_user = CustomUser.objects.filter(username='test').first()
        self.assertEqual(my_user.username, 'test')