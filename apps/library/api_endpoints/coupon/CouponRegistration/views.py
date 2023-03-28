import datetime

import pytz
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.library.api_endpoints.coupon.CouponRegistration.serializers import \
    CouponSerializer
from apps.library.choices import CartStatus
from apps.library.models import Cart, Coupon

utc = pytz.UTC

class CouponRegistrationView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CouponSerializer

    @swagger_auto_schema(request_body=CouponSerializer)
    def post(self, request, format=None):
        coupon_code = request.data["coupon_code"]
        try:
            coupon = Coupon.objects.get(code=coupon_code)
        except Coupon.DoesNotExist:
            raise Http404("Coupon does not exist")
        if coupon.expired_date > utc.localize(datetime.datetime.now()):
            try:
                cart = Cart.objects.get(user=request.user, status=CartStatus.PENDING)
                cart.status = CartStatus.CHECKOUT
                cart.save()
                serializer = self.serializer_class(coupon).data
                return Response(serializer)
            except Exception as e:
                return Response({"Error": f"{e}"})
        return Response({"error": "Coupon was expired"})


__all__ = ["CouponRegistrationView"]
