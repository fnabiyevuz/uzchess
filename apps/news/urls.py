from django.urls import path

from apps.news.views import NewsListApiView, NewsRetrieveAPIView

urlpatterns = [
    path("", NewsListApiView.as_view(), name="news-list"),
    path("<str:slug>", NewsRetrieveAPIView.as_view(), name="news-retrieve"),
]
