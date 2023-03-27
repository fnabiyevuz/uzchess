from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.course.models import Course
from apps.course.api_endpoints.course.CourseList.serializers import \
    CourseListSerializer
from apps.course.choices import SUCCESS


class GetPurchasedCoursesAPIView(ListAPIView):
    serializer_class = CourseListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Get Courses queryset purchased by request user
        """
        favourite_courses = Course.objects.filter(
            course_payment__user=self.request.user,
            course_payment__payment_status=SUCCESS
        )

        return favourite_courses
