from src.utils.tests.setup_tests import TestSetUp
from ..models import Category


class CategoryModelTest(TestSetUp):
    def test_creates_a_category(self):
        self.authenticate_user()
        category = self.fake.paragraph()
        new_category = Category(category=category)
        new_category.save()
        self.assertEqual(Category.objects.all().count(), 1)