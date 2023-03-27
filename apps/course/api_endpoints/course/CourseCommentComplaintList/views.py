from rest_framework import generics

from apps.course.models import CourseCommentComplaint

from .serializers import CourseCommentComplaintSerializer


class CourseCommentComplaintListAPIView(generics.ListAPIView):
    serializer_class = CourseCommentComplaintSerializer
    queryset = CourseCommentComplaint.objects.all()

    def get_queryset(self):
        comment_id = self.kwargs.get("comment_id")
        return self.queryset.filter(comment_id=comment_id).order_by("-id")
