from rest_framework import serializers

from apps.course.api_endpoints.course.CourseCommentList.serializers import \
    CourseCommentSerializer
from apps.course.models import CourseCommentComplaint
from apps.users.models import CustomUser


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "full_name", "avatar"]


class CourseCommentComplaintSerializer(serializers.ModelSerializer):
    is_mine = serializers.SerializerMethodField()
    user = UserShortSerializer()
    comment = CourseCommentSerializer()

    class Meta:
        model = CourseCommentComplaint
        fields = ["id", "user", "comment", "complaint_type", "complaint_text", "is_mine"]

    def get_is_mine(self, obj):
        return obj.user == self.context["request"].user
