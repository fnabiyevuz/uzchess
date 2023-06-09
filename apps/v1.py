from django.urls import include, path

urlpatterns = [
    path("common/", include("apps.common.urls")),
    path("course/", include("apps.course.urls")),
    path("library/", include("apps.library.urls")),
    path("main/", include("apps.main.urls")),
    path("news/", include("apps.news.urls")),
    path("users/", include("apps.users.urls")),
]
