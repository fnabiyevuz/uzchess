from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.library.api_endpoints.BookList.serializers import AuthorSerializer
from apps.library.models import Book
from apps.news.models import News


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ("id", "title", "slug", "photo", "context")


class BookSerializerForNews(ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ("id", "title", "author", "image")


class NewsRetrieveSerializer(ModelSerializer):
    views = SerializerMethodField()

    def get_views(self, news):
        return news.newsview_set.all().count()

    class Meta:
        model = News
        fields = ("id", "title", "photo", "context", "views", "created_at")
