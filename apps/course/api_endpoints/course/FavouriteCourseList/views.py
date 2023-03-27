from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView

from apps.course.models import FavouriteCourse

from .serializers import FavouriteCourseSerializer


class FavouriteCourseListAPIView(ListAPIView):
    serializer_class = FavouriteCourseSerializer
    queryset = FavouriteCourse.objects.all()

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        "course__title",
    ]
    filterset_fields = {"user": ["exact"]}

    def get(self, request, *args, **kwargs):
        """
        Returns all favourite courses
        """
        return self.list(request, *args, **kwargs)
