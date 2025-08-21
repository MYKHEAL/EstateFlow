from django.test import TestCase, Client
from django.urls import reverse
from .models import User


# Create your tests here.

class HouseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='hawanat',
            last_name='olamide',
            email="hawa@email.com",
            password="HawanaTestUser",
            username='hawanat',
        )
        self.client = Client()

    def test_that_anonymous_user_cannot_add_house_returns_403(self):
        self.client.login(username='hawanat', password="HawanaTestUser")
        url = reverse('add_house')
        data = {
            "house_number": 2,
            "address": "abule egba",
            "user": self.user.id
        }

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 403)