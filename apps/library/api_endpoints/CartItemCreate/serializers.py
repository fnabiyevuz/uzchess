from rest_framework.serializers import ModelSerializer

from apps.library.models import CartItem


class CartItemCreateSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = ("id", "book")
