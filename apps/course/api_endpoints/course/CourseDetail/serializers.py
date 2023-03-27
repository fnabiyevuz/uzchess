from django.db.models import Avg
from rest_framework import serializers

# from apps.common.serializers import SaleSerializer, ThumbnailImageSerializer
from apps.course.models import Chapter, Course, CourseCategory, CourseLevel


class CourseCategoryShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ["id", "title_uz", "title_ru", "title_en", "icon"]


class CourseLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLevel
        fields = ["id", "title_uz", "title_ru", "title_en", "icon"]


class CourseDetailSerializer(serializers.ModelSerializer):
    category = CourseCategoryShortSerializer()
    comments_count = serializers.SerializerMethodField()
    reviews_avg = serializers.SerializerMethodField()
    # chapters_count = serializers.SerializerMethodField()

    # is_bought = serializers.SerializerMethodField()
    # is_finished = serializers.SerializerMethodField()

    # sale = SaleSerializer()
    # thumbnail_cover_image = ThumbnailImageSerializer(source="cover_image")
    # left_comment = serializers.SerializerMethodField()

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
            # "chapters_count",
            # "is_bought",
            # "is_finished",
            # "left_comment",
        ]

        """checkIfThisUserFinishedCourse"""

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_reviews_avg(self, obj):
        return obj.comments.aggregate(avg=Avg("rating", default=0))["avg"]

    # def get_chapters_count(self, obj):
    #     return obj.chapters.count()

    # def get_is_bought(self, obj):
    #     user = self.context["request"].user
    #
    #     if not user.is_authenticated:
    #         return False
    #
    #     return obj.is_bought(user)
    #
    # def get_is_finished(self, obj):
    #     user = self.context["request"].user
    #
    #     if not user.is_authenticated:
    #         return False
    #
    #     return obj.is_finished(user)
    #
    # def get_left_comment(self, obj):
    #     user = self.context["request"].user
    #
    #     if not user.is_authenticated:
    #         return False
    #
    #     return obj.comments.filter(user=user).exists()
