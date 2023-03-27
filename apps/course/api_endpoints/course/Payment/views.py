from rest_framework.generics import ListAPIView

from apps.course.models import Payment

from .serializers import PaymentSerializer


class PaymentListAPIView(ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def get(self, request, *args, **kwargs):
        """
        Returns all payments
        """
        return self.list(request, *args, **kwargs)
