from rest_framework import generics
from rest_framework.generics import get_object_or_404

from apps.course.models import Course, VideoLesson

from .serializers import CourseVideoLessonListSerializer


class CourseVideoLessonListAPIView(generics.ListAPIView):
    serializer_class = CourseVideoLessonListSerializer
    queryset = VideoLesson.objects.all()

    # def get_object(self):
    #     return get_object_or_404(Course, pk=self.kwargs["course_id"], is_active=True)

    def get_object(self):
        return get_object_or_404(Course, pk=self.kwargs["course_id"])

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return VideoLesson.objects.none()
        return VideoLesson.objects.filter(course=self.get_object())
