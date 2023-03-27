from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.course.models import Payment, Course
from .serializers import PaymentCreateSerializer


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentCreateSerializer
    # queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = self.request.user
        course = Course.objects.get(id=self.kwargs['course_id'])
        payment = Payment.objects.filter(user=user, course=course)
        if len(payment) > 0:
            raise ValidationError('You have already bought for this course :)')
        if course.discounted_price > 0:
            payment = Payment.objects.create(user=user, course=course, amount=course.discounted_price)
        else:
            payment = Payment.objects.create(user=user, course=course, amount=course.price)

        serializer = self.get_serializer_class()(payment)
        print(serializer)
        return Response(serializer.data)
