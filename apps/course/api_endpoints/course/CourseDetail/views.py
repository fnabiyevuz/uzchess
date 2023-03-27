from rest_framework import generics
from rest_framework.exceptions import ValidationError

from apps.course.models import Course, UserCourse
from .serializers import CourseDetailSerializer


class CourseDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        user = self.request.user
        course = Course.objects.get(pk=self.kwargs['pk'])
        return UserCourse.objects.filter(user=user, course=course)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('You have already voted for this post :)')
        serializer.save(user=self.request.user, course=UserCourse.objects.get(pk=self.kwargs['pk']))


__all__ = ["CourseDetailAPIView"]
