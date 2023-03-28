from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from apps.library.models import Author, Book, Category


class BookDetailTestCase(TestCase):
    """Test module for GET book detail API"""

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

    def test_get_valid_book_detail(self):
        response = self.client.get(reverse("book-detail", kwargs={"pk": self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_book_detail(self):
        response = self.client.get(reverse("book-detail", kwargs={"pk": 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
