from rest_framework import serializers

from apps.course.models import CourseCategory


class CourseCategoryListSerializer(serializers.ModelSerializer):
    # courses_count = serializers.IntegerField()

    class Meta:
        model = CourseCategory
        # fields = ["id", "title_uz", "title_ru", "title_en", "icon", "courses_count"]

        fields = ["id", "title_uz", "title_ru", "title_en", "icon"]
