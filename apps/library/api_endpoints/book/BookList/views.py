from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from apps.library.api_endpoints.book.BookList.serializers import BookSerializer
from apps.library.models import Book


class BookListApiView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["language", "category", "level", "rate"]
    search_fields = ["title"]


__all__ = ["BookListApiView"]
