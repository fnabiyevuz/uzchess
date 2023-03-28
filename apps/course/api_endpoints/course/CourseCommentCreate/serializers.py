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

    def create(self, validated_data):
        comments = CourseComment.objects.filter(author=validated_data["author"], course=validated_data["course"])
        if len(comments) > 0:
            raise serializers.ValidationError(detail={"comment": _("You can't comment twice")}, code="unique")
        else:
            return super().create(validated_data)
