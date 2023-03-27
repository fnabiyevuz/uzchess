from rest_framework import serializers

from apps.library.models import Cart, CartItem, Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'image', )


class CartItemSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'name', 'image', )


class GetOrdersListSerializer(serializers.ModelSerializer):
    # items = serializers.SerializerMethodField()
    #
    # def get_items(self, cart):
    #     cart_items = cart.cartitem_set.all()
    #     serializer = CartItemSerializer(cart_items, many=True)
    #     return serializer.data

    class Meta:
        model = Cart
        fields = ('id', 'total',
                  # 'items'
                  )
