from src.utils.tests.setup_tests import TestSetUp
from src.api.users.models import User
from rest_framework import status
    
class TestViews(TestSetUp):
    def test_shouldnot_create_a_registry_when_unauthenticated(self):
        res = self.client.post(self.registries_url, { 'title': "Test title", 'description': "Test description", 'type': "Income", 'amount': 133.99 })
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_should_create_a_registry(self):
        user = self.authenticate_user()
        category = self.create_category()
        currency = self.create_currency()
        res = self.client.post(self.registries_url, { 'title': "Test title", 'description': "Test description", 'currency': currency.id, 'type': "Income", 'amount': 133.99, 'category': category.id, 'user': user.id })
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_paginates_registry_by_pages(self):
        self.authenticate_user()
        response = self.client.get(self.registries_url + "?show_meta=1")
        self.assertEqual(response.data['results'], [])
        self.assertEqual(response.data['count'], 0)