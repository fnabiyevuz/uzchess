from django.urls import path

from apps.main.views import FeedbackCreateApiView, get_info, get_rulesofuseing

urlpatterns = [
    path('info/', get_info, name='info'),
    path('feedback/create/', FeedbackCreateApiView.as_view(), name='feedback-create'),
    path('rules/', get_rulesofuseing, name='rulesofusing'),

]
