from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.library.models import Author, Book, Category


# Define the test class for the Book API
class BookAPITestCase(APITestCase):
    def setUp(self):
        author = Author.objects.create(full_name="Test Author")
        category = Category.objects.create(title="Test Category")
        self.book = Book.objects.create(
            author=author,
            title="Test Book",
            page=100,
            published_year=2022,
            description="This is a test book.",
            image="test_image.jpg",
            price=10.99,
            discount=1.00,
            rate=4.5,
            category=category,
            language="en",
            level="elementary",
        )

    def test_get_all_books(self):
        url = reverse("book-lists")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
