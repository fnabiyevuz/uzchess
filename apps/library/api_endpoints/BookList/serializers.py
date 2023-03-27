from rest_framework.serializers import ModelSerializer

from apps.library.models import Author, Book, Category


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "full_name")


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title")


class BookSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Book
        fields = ("id", "title", "author", "image", "price", "discount", "level", "category", "rate", "language")
