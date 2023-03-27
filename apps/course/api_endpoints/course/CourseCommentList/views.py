from rest_framework import generics

from apps.course.models import CourseComment

from .serializers import CourseCommentSerializer


class CourseCommentListAPIView(generics.ListAPIView):
    serializer_class = CourseCommentSerializer
    queryset = CourseComment.objects.all()

    def get_queryset(self):
        course_id = self.kwargs.get("course_id")
        return self.queryset.filter(course_id=course_id).order_by("-id")
