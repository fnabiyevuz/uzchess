from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.course.models import CourseCommentComplaint


class CourseCommentComplaintCreateSerializer(serializers.ModelSerializer):
    # is_mine = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source="user.username")

    # user = UserShortSerializer()
    # comment = CourseCommentSerializer()

    class Meta:
        model = CourseCommentComplaint
        fields = [
            "id",
            "comment",
            "user",
            "complaint_type",
            "complaint_text",
            # "is_mine"
        ]
        read_only_fields = [
            "id",
            "user",
            # "is_mine"
        ]

    def create(self, validated_data):
        comments = CourseCommentComplaint.objects.filter(user=validated_data["user"], comment=validated_data["comment"])
        if len(comments) > 0:
            raise serializers.ValidationError(detail={"comment": _("You can't comment twice")}, code="unique")
        else:
            return super().create(validated_data)
