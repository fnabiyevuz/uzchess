from rest_framework import serializers

from apps.course.models import CourseComment
from apps.library.api_endpoints.BookList.serializers import AuthorSerializer
from apps.users.models import CustomUser


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "full_name"]


class CourseCommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = CourseComment
        fields = ["id", "author", "rating", "comment_text", "created_at"]
