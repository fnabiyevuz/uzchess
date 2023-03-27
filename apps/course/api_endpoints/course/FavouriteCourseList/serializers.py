from rest_framework.serializers import ModelSerializer

from apps.course.models import FavouriteCourse


class FavouriteCourseSerializer(ModelSerializer):
    class Meta:
        model = FavouriteCourse
        fields = [
            "id",
            "course",
            "user",
        ]
