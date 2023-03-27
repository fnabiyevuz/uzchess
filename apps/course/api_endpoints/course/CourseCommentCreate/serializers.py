from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.course.models import CourseComment, UserCourse


class CourseCommentCreateSerializer(serializers.ModelSerializer):
    # is_mine = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = CourseComment
        fields = [
            "id",
            "author",
            "rating",
            "comment_text",
            "status",
            # "is_mine"
        ]
        read_only_fields = ["id", "author"]

    # def create(self, validated_data):
    #     if not UserCourse.objects.filter(
    #         author=validated_data["author"], course=validated_data["course"], is_finished=True
    #     ).exists():
    #         raise serializers.ValidationError(detail={"course": _("You must finish the course")}, code="not_permitted")
    #     if CourseComment.objects.filter(author=validated_data["author"], course=validated_data["course"]).exists():
    #         raise serializers.ValidationError(detail={"comment": _("You can't comment twice")}, code="unique")
    #     return super().create(validated_data)

    # def get_is_mine(self, obj):
    #     return obj.user == self.context["request"].user
