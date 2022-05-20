import pytest
from django.test import Client, TestCase
from django.urls import reverse


@pytest.mark.django_db
class TestIndex(TestCase):
    client = Client()

    def test_index(self):
        url = reverse('index')
        self.checkAssertion(url, b"Welcome")

    def checkAssertion(self, url, arg1):
        response = self.client.get(url)
        assert arg1 in response.content
        assert response.status_code == 200
