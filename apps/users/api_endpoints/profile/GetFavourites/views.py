from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.library.api_endpoints.BookList.serializers import \
    BookSerializer as BookListSerializer
from apps.library.models import Book


class GetFavouriteBooksAPIView(ListAPIView):
    serializer_class = BookListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Get Books queryset liked by request user
        """
        favourite_books = Book.objects.filter(favourite_books__user=self.request.user)

        return favourite_books


__all__ = ["GetFavouriteBooksAPIView"]
