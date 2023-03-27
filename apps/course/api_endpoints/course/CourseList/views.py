from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView

from apps.course.models import Course

from .serializers import CourseListSerializer


class CourseListApiView(ListAPIView):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        "title",
    ]
    # filterset_fields = {"category": ["in"], "type": ["exact"]}

    def get(self, request, *args, **kwargs):
        """
        Returns all active courses
        """
        return self.list(request, *args, **kwargs)


__all__ = ["CourseListApiView"]
