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

    # def create(self, validated_data):
    #     if not UserCourse.objects.filter(
    #             user=validated_data["user"], course=validated_data["course"], is_finished=True
    #     ).exists():
    #         raise serializers.ValidationError(detail={"course": _("You must finish the course")}, code="not_permitted")
    #     if CourseCommentComplaint.objects.filter(user=validated_data["user"], course=validated_data["course"]).exists():
    #         raise serializers.ValidationError(detail={"comment": _("You can't comment twice")}, code="unique")
    #     return super().create(validated_data)

    # def get_is_mine(self, obj):
    #     return obj.user == self.context["request"].user
