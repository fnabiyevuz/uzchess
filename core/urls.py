from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

from .schema import swagger_urlpatterns


urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path('api/v1/', include('apps.v1')),
    path("ckeditor/", include("ckeditor_uploader.urls"))
]

urlpatterns += swagger_urlpatterns
urlpatterns += i18n_patterns(path("admin/", admin.site.urls))

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
