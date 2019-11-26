from django.test import TestCase
from .models import Site, Tag
from django.contrib.auth import get_user_model
# Create your tests here.
class TestSite(TestCase):
    def setUp(self):
        
        tag = Tag.objects.first()
        user = get_user_model().objects.first()
        
        self.site = Site(
            cover='default.jpg',
            title='test site',
            description='This is test site',
            author=user,
            link='http://localhost:5000/django'
        )

        self.site.tags.set(tag)

    # def test_get_absolute_url(self):
    #     self.assertEqual(self.user.get_absolute_url(), '/accounts/user/1/')

    def test_is_instance(self):
        self.assertIsInstance(self.site, Site)

    # def test_user_is_saved(self):
    #     test_user = get_user_model().objects.create_user(
    #         username = "test",
    #         email = "dummy@test.com",
    #         password = 'secret'
    #     )
    #     test_user.save()
    #     my_user = CustomUser.objects.filter(username='test').first()
    #     self.assertEqual(my_user.username, 'test')