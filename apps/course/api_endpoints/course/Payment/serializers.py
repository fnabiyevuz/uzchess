from rest_framework import serializers

from apps.course.api_endpoints.course.CourseList.serializers import \
    CourseListSerializer
from apps.course.models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = [
            "id",
            "usercourse",
            "payment_type",
            "payment_status",
            "amount",
            "payment_date",
            "created_at",
        ]

    """check is user already bought this course"""

    def checkIfThisUserAlreadyBoughtThisCourse(self, course_id, user_id):
        if Payment.objects.filter(course_id=course_id, user_id=user_id).exists():
            return True
        else:
            return False
