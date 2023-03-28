from django.utils.duration import duration_string
from rest_framework import serializers

# from apps.common.serializers import SaleSerializer, ThumbnailImageSerializer
from apps.course.models import Chapter, VideoLesson


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = [
            "id",
            "title",
        ]


class CourseVideoLessonListSerializer(serializers.ModelSerializer):
    # sale = SaleSerializer()
    chapter = ChapterSerializer()
    is_bought = serializers.SerializerMethodField()
    # video = serializers.SerializerMethodField()
    last_watched_time = serializers.SerializerMethodField()

    # thumbnail_cover_image = ThumbnailImageSerializer(source="cover_image")

    class Meta:
        model = VideoLesson
        fields = [
            "id",
            "title",
            "chapter",
            "video_duration",
            "is_bought",
            "last_watched_time",
            "video_thumbnail",
        ]

    def get_is_bought(self, obj):
        user = self.context["request"].user

        if not user.is_authenticated:
            return False

        return obj.is_bought(user)

    def get_last_watched_time(self, obj):
        user = self.context["request"].user

        if not user or not user.is_authenticated:
            return

        return duration_string(obj.get_user_last_watched_time(user))
