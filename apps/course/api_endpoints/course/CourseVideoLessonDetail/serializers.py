from django.utils.duration import duration_string
from rest_framework import serializers

# from apps.common.serializers import SaleSerializer, ThumbnailImageSerializer
from apps.course.models import Chapter, VideoLesson, VideoUserViews


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = [
            "id",
            "title",
        ]

class CourseVideoLessonListShortSerializer(serializers.ModelSerializer):
    is_viewed = serializers.SerializerMethodField()

    def get_is_viewed(self, obj):
        if VideoUserViews.objects.filter(user=self.context['request'].user, video=obj, is_finished=True).exists():
            return True
        else:
            return False


    class Meta:
        model = VideoLesson
        fields = [
            "id",
            "title",
            "video_path",
            "video_thumbnail",
            "is_viewed"
        ]


class CourseVideoLessonListSerializer(serializers.ModelSerializer):
    # sale = SaleSerializer()
    chapter = ChapterSerializer()
    lessons = serializers.SerializerMethodField()
    # is_bought = serializers.SerializerMethodField()
    # video = serializers.SerializerMethodField()
    # last_watched_time = serializers.SerializerMethodField()

    # thumbnail_cover_image = ThumbnailImageSerializer(source="cover_image")

    class Meta:
        model = VideoLesson
        fields = [
            "id",
            "title",
            "chapter",
            "video_duration",
            # "is_bought",
            "video_path",
            # "last_watched_time",
            "lessons",
            "video_thumbnail",
        ]

    # def get_is_bought(self, obj):
    #     user = self.context["request"].user
    #
    #     if not user.is_authenticated:
    #         return False
    #
    #     return obj.is_bought(user)

    # def get_last_watched_time(self, obj):
    #     user = self.context["request"].user
    #
    #     if not user or not user.is_authenticated:
    #         return
    #
    #     return duration_string(obj.get_user_last_watched_time(user))


    def get_lessons(self, obj):
        print(self.context["request"])
        videos = obj.chapter.chapter.all()
        serializer = CourseVideoLessonListShortSerializer(videos, many=True, context={"request": self.context["request"]})
        return serializer.data