from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from apps.course.models import Course, CourseComment

from .serializers import CourseCommentCreateSerializer


class CourseCommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseCommentCreateSerializer
    queryset = CourseComment.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        course = get_object_or_404(Course, id=self.kwargs.get("course_id"))
        serializer.save(author=self.request.user, course=course)
