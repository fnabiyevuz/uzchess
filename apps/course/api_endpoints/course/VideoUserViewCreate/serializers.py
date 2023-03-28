from rest_framework import serializers

from apps.course.models import VideoUserViews


class VideoUserViewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoUserViews
        fields = [
            "id",
            "video",
            "user",
            "is_finished",
        ]
