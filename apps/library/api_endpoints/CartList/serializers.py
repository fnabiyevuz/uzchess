from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.library.models import Book, Cart, CartItem


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "image", "price", "discount")


class CartItemSerializer(ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ("id", "book", "quantity", "total")


class CartDetailSerializer(ModelSerializer):
    items = SerializerMethodField()

    def get_items(self, cart):
        cart_items = cart.cartitem_set.all()
        serializer = CartItemSerializer(cart_items, many=True).data
        return serializer

    class Meta:
        model = Cart
        fields = ("id", "total", "coupon", "items")
