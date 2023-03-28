from rest_framework.serializers import ModelSerializer

from apps.course.models import Course, CourseCategory


class CourseCategorySerializer(ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ["id", "title", "icon"]


class CourseListSerializer(ModelSerializer):
    category = CourseCategorySerializer(read_only=True)

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
        ]
