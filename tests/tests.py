import random

from django.conf import settings
from django.test import TestCase, override_settings

from django_spam import SPAM_ROUTES


class DjangoSpamTestCase(TestCase):
    def test_redirect_random_route(self):
        response = self.client.get('/'+random.choice(SPAM_ROUTES))
        self.assertEqual(response.status_code, 302)
    

    def test_add_spam_routes_in_settings(self):
        spam_routes = getattr(settings, 'SPAM_ROUTES', [])
        response = self.client.get('/'+spam_routes[-1])
        self.assertEqual(response.status_code, 302)