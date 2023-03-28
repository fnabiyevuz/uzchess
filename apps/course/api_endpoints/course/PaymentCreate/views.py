from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.course.models import Course, Payment

from .serializers import PaymentCreateSerializer


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentCreateSerializer
    # queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = self.request.user
        course = self.request.data.get('course')
        payment_type = self.request.data.get('payment_type')
        payment_status = self.request.data.get('payment_status')
        payment = Payment.objects.filter(user=user, course=course)
        if len(payment) > 0:
            raise ValidationError("You have already bought for this course :)")
        if payment_status == "success":
            if course.discounted_price > 0:
                payment = Payment.objects.create(user=user, course=course, amount=course.discounted_price, payment_type=payment_type)
            else:
                payment = Payment.objects.create(user=user, course=course, amount=course.price, payment_type=payment_type)

        serializer = self.get_serializer_class()(payment)
        print(serializer)
        return Response(serializer.data)
