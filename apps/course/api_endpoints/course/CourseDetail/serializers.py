from django.db.models import Avg
from rest_framework import serializers
# from apps.common.serializers import SaleSerializer, ThumbnailImageSerializer
from tinycss2 import serializer

from apps.course.api_endpoints.course import CourseCommentSerializer
from apps.course.api_endpoints.course.CourseVideoLessonDetail.serializers import \
    ChapterSerializer
from apps.course.models import (Chapter, Course, CourseCategory, CourseLevel,
                                UserCourse, VideoLesson)


class CourseCategoryShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ["id", "title", "icon"]


class CourseLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLevel
        fields = ["id", "title", "icon"]


class VideoLessonForCourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLesson
        fields = [
            "id",
            "title",
            "video_path",
        ]


class ChapterForCourseDetailSerializer(serializers.ModelSerializer):
    video_lessons = serializers.SerializerMethodField()

    def get_video_lessons(self, obj):
        serializer = VideoLessonForCourseDetailSerializer(obj.chapter.all(), many=True)
        return serializer.data

    class Meta:
        model = Chapter
        fields = [
            "id",
            "title",
            "video_lessons",
        ]


class CourseDetailSerializer(serializers.ModelSerializer):
    category = CourseCategoryShortSerializer()
    comments_count = serializers.SerializerMethodField()
    reviews_avg = serializers.SerializerMethodField()
    is_bought = serializers.SerializerMethodField()
    chapters = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    # is_bought = serializers.SerializerMethodField()
    # is_finished = serializers.SerializerMethodField()

    # sale = SaleSerializer()
    # thumbnail_cover_image = ThumbnailImageSerializer(source="cover_image")
    # left_comment = serializers.SerializerMethodField()

    def get_is_bought(self, obj):
        if UserCourse.objects.filter(user=self.context["request"].user, course=obj).exists():
            return True
        return False

    def get_chapters(self, obj):
        serializer = ChapterForCourseDetailSerializer(obj.course.all(), many=True)
        return serializer.data

    def get_comments(self, obj):
        serializer = CourseCommentSerializer(obj.comments.all(), many=True)
        return serializer.data

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "author",
            "lang_code",
            "price",
            "discounted_price",
            "discounted_expire_date",
            "category",
            "level",
            "comments_count",
            "reviews_avg",
            "chapters",
            "is_bought",
            "comments",
            # "is_finished",
            # "left_comment",
        ]

        """checkIfThisUserFinishedCourse"""

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_reviews_avg(self, obj):
        return obj.comments.aggregate(avg=Avg("rating", default=0))["avg"]
