# Doit assurer le test de l'index
"""

chaque test doit demander l'URI correspondant, qui ne doit pas être codé en dur, par exemple utiliser lettings:index et la fonction reverse au lieu d’utiliser /lettings,
comme chaque page du site contient un élément de titre, chaque test doit le vérifier dans le HTML de la réponse ;


"""
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