from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apps.course.models import Chapter, Course, VideoLesson

from .serializers import CourseVideoLessonListSerializer


class CourseVideoLessonDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CourseVideoLessonListSerializer
    queryset = VideoLesson.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CourseVideoLessonListSerializer(instance, context={"request": request})
        return Response(serializer.data)

    # def get_object(self):
    #     return get_object_or_404(Chapter, pk=self.kwargs["chapter_id"])
    #
    # def get_queryset(self):
    #     if getattr(self, "swagger_fake_view", False):
    #         return VideoLesson.objects.none()
    #     return VideoLesson.objects.filter(chapter=self.get_object())
