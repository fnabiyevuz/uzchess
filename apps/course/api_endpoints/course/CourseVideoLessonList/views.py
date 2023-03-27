from rest_framework import generics
from rest_framework.generics import get_object_or_404

from apps.course.models import Course, VideoLesson, Chapter

from .serializers import CourseVideoLessonListSerializer


class CourseVideoLessonListAPIView(generics.ListAPIView):
    serializer_class = CourseVideoLessonListSerializer
    queryset = VideoLesson.objects.all()

    # def get_object(self):
    #     return get_object_or_404(Chapter, pk=self.kwargs["chapter_id"])
    #
    # def get_queryset(self):
    #     if getattr(self, "swagger_fake_view", False):
    #         return VideoLesson.objects.none()
    #     return VideoLesson.objects.filter(chapter=self.get_object())
