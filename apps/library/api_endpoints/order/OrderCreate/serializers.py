from rest_framework.serializers import ModelSerializer

from apps.library.models import Order


class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "cart",
            "full_name",
            "phone",
            "email",
            "payment_status",
            "payment_type",
            "coupon",
            "order_id",
            "payment_amount",
        )
