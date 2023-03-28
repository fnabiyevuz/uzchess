from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.course.models import VideoUserViews

from .serializers import VideoUserViewCreateSerializer


class VideoUserViewCreateAPIView(generics.CreateAPIView):
    serializer_class = VideoUserViewCreateSerializer
    queryset = VideoUserViews.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['user'] = self.request.user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
