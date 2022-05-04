from src.utils.tests.setup_tests import TestSetUp
from rest_framework import status

class TestViews(TestSetUp):
    def test_shouldnot_create_a_currency_unauthenticated(self):
        res = self.client.post(self.currencies_url, { 'symbol': "TEST", 'description': "Currency description" })
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_should_create_a_currency(self):
        self.authenticate_user()
        res = self.client.post(self.currencies_url, { 'symbol': "TEST", 'description': "Currency description" })
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_paginates_currency_by_pages(self):
        self.authenticate_user()
        response = self.client.get(self.currencies_url + "?show_meta=1")
        self.assertEqual(response.data['results'], [])
        self.assertEqual(response.data['count'], 0)