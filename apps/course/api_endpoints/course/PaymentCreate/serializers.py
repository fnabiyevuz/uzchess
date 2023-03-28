from rest_framework import serializers

from apps.course.models import Payment


class PaymentCreateSerializer(serializers.Serializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "user",
            "course",
            "payment_type",
            "payment_status",
            "amount",
            "payment_date",
            "created_at",
        ]
