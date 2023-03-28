from rest_framework.serializers import ModelSerializer

from apps.course.models import UserCourse


class UserCourseSerializer(ModelSerializer):
    class Meta:
        model = UserCourse
        fields = ("id", "user", "course")
