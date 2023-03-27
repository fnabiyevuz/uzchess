from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from apps.course.models import Course, CourseComment, CourseCommentComplaint

from .serializers import CourseCommentComplaintCreateSerializer


class CourseCommentComplaintCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseCommentComplaintCreateSerializer
    queryset = CourseCommentComplaint.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        comment = get_object_or_404(CourseComment, id=self.kwargs.get("comment_id"))
        serializer.save(user=self.request.user, comment=comment)
