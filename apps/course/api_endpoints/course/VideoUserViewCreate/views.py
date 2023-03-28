from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.course.models import VideoUserViews
from .serializers import VideoUserViewCreateSerializer


class VideoUserViewCreateAPIView(generics.CreateAPIView):
    serializer_class = VideoUserViewCreateSerializer
    queryset = VideoUserViews.objects.all()
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
