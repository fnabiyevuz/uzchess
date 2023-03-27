from django.db.models import Count, Q
from rest_framework import filters, permissions
from rest_framework.generics import ListAPIView

from apps.course.api_endpoints.course_category.CourseCategoryListApi.serializers import \
    CourseCategoryListSerializer
from apps.course.models import CourseCategory


class CourseCategoryListApiView(ListAPIView):
    serializer_class = CourseCategoryListSerializer
    permission_classes = [permissions.AllowAny]
    search_fields = ["title"]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    queryset = CourseCategory.objects.all()
    # def get_queryset(self):
    #     return CourseCategory.objects.annotate(courses_count=Count("courses", filter=Q(courses__is_active=True)))
