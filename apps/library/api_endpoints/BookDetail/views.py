from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from apps.library.api_endpoints.BookDetail.serializers import \
    BookDetailSerializer
from apps.library.api_endpoints.BookList.serializers import BookSerializer
from apps.library.models import Book


class BookDetailApiView(RetrieveAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance).data
        books = self.queryset.filter(category=instance.category).exclude(id=instance.id).order_by("-rate")[:5]
        books_serializer = BookSerializer(books, many=True).data
        return Response({"detail": serializer, "recommended": books_serializer})


__all__ = ["BookDetailApiView"]
