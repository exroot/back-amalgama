from src.utils.tests.setup_tests import TestSetUp
from ..models import User

class UserModelTest(TestSetUp):
    def test_creates_a_user(self):
        self.authenticate_admin()
        user = User(**self.admin_data_2)
        user.save()
        self.assertEqual(User.objects.all().count(), 2)