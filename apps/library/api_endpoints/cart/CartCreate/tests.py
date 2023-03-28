from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.library.choices import CartStatus
from apps.library.models import Author, Cart, Category
from apps.users.choices import AUTH_TYPES
from apps.users.models import CustomUser


# Define the test class for the Cart API
class CartAPITestCase(APITestCase):
    def setUp(self):
        user = CustomUser.objects.create(
            full_name='Test Test',
            auth_type='via email'
        )
        self.cart = Cart.objects.create(
            user=user
        )

    def test_cart_defaults(self):
        self.assertEqual(self.cart.status, CartStatus.PENDING)

