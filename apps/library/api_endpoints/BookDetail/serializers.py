from rest_framework.serializers import ModelSerializer

from apps.library.api_endpoints.BookList.serializers import AuthorSerializer, CategorySerializer
from apps.library.models import Book


class BookDetailSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'image', 'price', 'discount', 'level', 'category', 'rate', 'language', 'description', 'published_year', 'page')
