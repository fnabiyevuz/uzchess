import json

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.library.models import Author, Book, Category


@pytest.mark.django_db
def test_book_list(api_client, book_factory):
    # Create some books using the factory
    book_factory.create_batch(5)

    # Get the URL for the book list view
    url = reverse("book-lists")

    # Make the request and check the response
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

    # Decode the response JSON and check the results
    data = json.loads(response.content)
    assert len(data) == 5


@pytest.mark.django_db
def test_book_detail(api_client, book_factory):
    # Create a book using the factory
    book = book_factory()

    # Get the URL for the book detail view
    url = reverse("book-detail", args=[book.id])

    # Make the request and check the response
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

    # Decode the response JSON and check the results
    data = json.loads(response.content)
    assert data["title"] == book.title


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def author_factory():
    def factory(**kwargs):
        return Author.objects.create(full_name="Test Author", **kwargs)

    return factory


@pytest.fixture
def category_factory():
    def factory(**kwargs):
        return Category.objects.create(title="Test Category", **kwargs)

    return factory


@pytest.fixture
def book_factory(author_factory, category_factory):
    def factory(**kwargs):
        author = author_factory()
        category = category_factory()
        defaults = {
            "author": author,
            "category": category,
            "title": "Test Book",
            "description": "Test Description",
            "price": 10.0,
        }
        defaults.update(kwargs)
        return Book.objects.create(**defaults)

    return factory
