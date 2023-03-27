from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from apps.library.models import Book
from apps.news.models import News, NewsView
from apps.news.serializers import NewsSerializer, NewsRetrieveSerializer, BookSerializerForNews
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters


class NewsListApiView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']



class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsRetrieveSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        device_id = self.request.META.get('HTTP_USER_AGENT', '')
        if request.user.is_authenticated:
            if device_id is not None:
                NewsView.objects.update_or_create(
                    news=instance,
                    user=request.user,
                    device_id=device_id
                )
            NewsView.objects.update_or_create(
                news=instance,
                user=request.user
            )
        elif device_id is not None:
            NewsView.objects.update_or_create(
                news=instance,
                device_id=device_id
            )
        return Response(serializer.data)
