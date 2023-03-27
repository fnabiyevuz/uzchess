from rest_framework.serializers import ModelSerializer

from apps.library.models import Cart


class CartUpdateSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'full_name', 'phone', 'email', 'coupon')
