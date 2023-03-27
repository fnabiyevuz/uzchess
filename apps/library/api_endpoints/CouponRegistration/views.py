import datetime

from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.library.api_endpoints.CouponRegistration.serializers import \
    CouponSerializer
from apps.library.models import Coupon


class CouponRegistrationView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CouponSerializer

    def post(self, request, format=None):
        coupon_code = request.data["coupon_code"]
        try:
            coupon = Coupon.objects.get(code=coupon_code)
        except Coupon.DoesNotExist:
            raise Http404("Coupon does not exist")
        if coupon.expired_date > datetime.datetime.now():
            serializer = self.serializer_class(coupon).data
            return Response(serializer)
        return Response({"error": "Coupon was expired"})


__all__ = ["CouponRegistrationView"]
