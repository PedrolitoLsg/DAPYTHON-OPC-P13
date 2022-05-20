import pytest
from django.test import Client, TestCase
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestProfiles(TestCase):
    client = Client()

    def test_profiles_index(self):
        url = reverse('profiles_index')
        self.checkAssertion(url, b"Profiles")

    def test_profile_detail(self):
        user = User.objects.create_user(username='JohnDoe',
                                        first_name='Doe',
                                        last_name='John',
                                        email='john@doe.com')
        profile = Profile.objects.create(
            user=user,
            favorite_city='Lima'
        )
        url = reverse('profile', args=[profile.user.username])
        self.checkAssertion(url, b'Lima')

    def checkAssertion(self, url, arg1):
        response = self.client.get(url)
        assert arg1 in response.content
        assert response.status_code == 200
