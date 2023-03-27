from rest_framework.serializers import ModelSerializer

from apps.library.models import Coupon


class CouponSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        fields = ("code", "percent", "min_amount", "expired_date")
