from rest_framework import generics

from apps.course.models import Course
from .serializers import CourseDetailSerializer


class CourseDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()


__all__ = ["CourseDetailAPIView"]
