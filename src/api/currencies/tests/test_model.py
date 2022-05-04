from src.utils.tests.setup_tests import TestSetUp
from ..models import Currency


class CurrencyModelTest(TestSetUp):
    def test_creates_a_currency(self):
        self.authenticate_user()
        symbol = self.fake.word()
        description = self.fake.sentence()
        currency = Currency(symbol=symbol, description=description)
        currency.save()
        self.assertEqual(Currency.objects.all().count(), 1)