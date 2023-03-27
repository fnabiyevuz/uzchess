from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from .schema import swagger_urlpatterns

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("api/v1/", include("apps.v1")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    # path("api/v1/course/", include("apps.course.urls")),
]
urlpatterns += swagger_urlpatterns
urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
urlpatterns += swagger_urlpatterns

if "rosetta" in settings.INSTALLED_APPS:
    urlpatterns += [re_path(r"^rosetta/", include("rosetta.urls"))]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
