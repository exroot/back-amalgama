from src.utils.tests.setup_tests import TestSetUp
from ..models import Registry

class RegistryModelTest(TestSetUp):
    def test_creates_a_currency(self):
        user = self.authenticate_user()
        title = self.fake.sentence()
        description = self.fake.sentence()
        currency = self.create_currency()
        type = 'Income'
        amount = self.fake.random_digit()
        category = self.create_category()
        registry = Registry(user=user, title=title, description=description, currency=currency, type=type, amount=amount, category=category)
        registry.save()
        self.assertEqual(Registry.objects.all().count(), 1)