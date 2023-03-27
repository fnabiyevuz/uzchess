from rest_framework import serializers

from apps.course.models import CourseComment
from apps.users.models import CustomUser


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "full_name"]


class CourseCommentSerializer(serializers.ModelSerializer):
    # is_mine = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    class Meta:
        model = CourseComment
        # fields = ["id", "author", "rating", "status", "comment_text", "is_mine"]
        fields = ["id", "author", "rating", "status", "comment_text"]

    # def get_is_mine(self, obj):
    #     return obj.author == self.context["request"].author

    def get_author(self, obj):
        return UserShortSerializer(obj.author, context=self.context).data
