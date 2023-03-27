from rest_framework.serializers import CharField, Serializer


class CouponSerializer(Serializer):
    code = CharField(max_length=9)
