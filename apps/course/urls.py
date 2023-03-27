from django.urls import path

from .api_endpoints import course, course_category

app_name = "course"

urlpatterns = [
    # course list
    path("CourseList", course.CourseListApiView.as_view(), name="course-list"),
    path(
        "CourseCategoryList",
        course_category.CourseCategoryListApiView.as_view(),
        name="course-category-list",
    ),
    path("CourseDetail/<int:pk>", course.CourseDetailAPIView.as_view(), name="course-detail"),
    # course video lessons
    path(
        "CourseVideoLessonList/<int:course_id>",
        course.CourseVideoLessonListAPIView.as_view(),
        name="course-video-lesson-list",
    ),
    # course comments
    path("CourseCommentList/<int:course_id>", course.CourseCommentListAPIView.as_view(), name="course-comment-list"),
    path(
        "CourseCommentCreate/<int:course_id>", course.CourseCommentCreateAPIView.as_view(), name="course-comment-create"
    ),
    # course comment complaints
    path(
        "CourseCommentComplaintList/<int:comment_id>",
        course.CourseCommentComplaintListAPIView.as_view(),
        name="course-complaint-list",
    ),
    path(
        "CourseCommentComplaintCreate/<int:comment_id>",
        course.CourseCommentComplaintCreateAPIView.as_view(),
        name="course-complaint-create",
    ),
    # certificate
    path("GenerateCertificate", course.GenerateCertificateAPIView.as_view(), name="generate-certificate"),
    # payment
    path("PaymentList", course.PaymentListAPIView.as_view(), name="payment-list"),
]
