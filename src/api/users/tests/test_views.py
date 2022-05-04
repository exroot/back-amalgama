from src.utils.tests.setup_tests import TestSetUp
from src.api.users.models import User
from rest_framework import status
    
class TestViews(TestSetUp):
    def test_shouldnot_create_a_user_when_unauthenticated(self):
        res = self.client.post(self.users_url, self.user_data)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_shouldnot_create_a_user(self):
        self.authenticate_user()
        res = self.client.post(self.users_url, self.user_data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_paginates_users_by_pages(self):
        self.authenticate_admin()
        response = self.client.get(self.registries_url + "?show_meta=1")
        self.assertEqual(response.data['results'], [])
        self.assertEqual(response.data['count'], 0)