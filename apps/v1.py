from django.urls import path, include

urlpatterns = [
    path('cart/', include('apps.cart.urls')),
    path('common/', include('apps.common.urls')),
    path('course/', include('apps.course.urls')),
    path('feedback/', include('apps.feedback.urls')),
    path('library/', include('apps.library.urls')),
    path('main/', include('apps.main.urls')),
    path('news/', include('apps.news.urls')),
    # path('users/', include('apps.users.urls')),
]
