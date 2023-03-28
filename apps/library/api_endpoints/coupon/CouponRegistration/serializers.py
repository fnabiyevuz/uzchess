from rest_framework.serializers import ModelSerializer

from apps.library.models import Coupon



class CouponSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        fields = ("id", "code", "percent", "min_amount", "expired_date")
        read_only_fields = ("id", "percent", "min_amount", "expired_date")