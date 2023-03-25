from rest_framework.serializers import Serializer, CharField


class CouponSerializer(Serializer):
    code = CharField(max_length=9)

