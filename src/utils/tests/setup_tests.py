from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker
from src.api.categories.models import Category
from src.api.currencies.models import Currency
from src.api.users.models import User


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('authentication:register')
        self.login_url = reverse('authentication:login')
        self.logout_url = reverse('authentication:logout')
        self.categories_url = reverse('categories:categories')
        self.currencies_url = reverse('currencies:currencies')
        self.registries_url = reverse('registries:registries')
        self.users_url = reverse('users:users')

        self.fake = Faker()

        self.user_data = {
            'email': self.fake.email(),
            'password': self.fake.email(),
            'is_active': True,
            'profile_image': self.fake.url(),
            'date_of_birth': self.fake.date(),
            'name': self.fake.name()
        }
        self.admin_data = {
            'email': self.fake.email(),
            'password': self.fake.email(),
            'is_active': True,
            'profile_image': self.fake.url(),
            'date_of_birth': self.fake.date(),
            'name': self.fake.name(),
            'is_admin': True
        }

        self.admin_data_2 = {
            'email': self.fake.email(),
            'password': self.fake.email(),
            'is_active': True,
            'profile_image': self.fake.url(),
            'date_of_birth': self.fake.date(),
            'name': self.fake.name(),
            'is_admin': True
        }

        self.category_data = { 'category': "Test category" }
        self.currency_data = { 'symbol': "TEST", 'description': "Currency description" }

        return super().setUp()

    def create_test_admin(self):
        res = self.client.post(
            self.register_url, self.admin_data)
        user = User.objects.get(email=res.data['email'])
        return user

    def create_test_user(self):
        res = self.client.post(
            self.register_url, self.user_data)
        user = User.objects.get(email=res.data['email'])
        return user

    def create_category(self):
        self.client.post(
            self.categories_url, self.category_data)
        category = Category.objects.first()
        return category

    def create_currency(self):
        self.client.post(
            self.currencies_url, self.currency_data)
        currency = Currency.objects.first()
        return currency

    def authenticate_user(self):
        self.client.post(
            self.register_url, self.user_data)
        res = self.client.post(self.login_url, self.user_data)
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + res.data['tokens']['access'])

        user = User.objects.get(email=res.data['email'])
        return user

    def authenticate_admin(self):
        self.client.post(
            self.register_url, self.admin_data)
        res = self.client.post(
            self.login_url, self.admin_data)
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + res.data['tokens']['access'])

        admin = User.objects.get(email=res.data['email'])
        return admin

    def tearDown(self):
        return super().tearDown()