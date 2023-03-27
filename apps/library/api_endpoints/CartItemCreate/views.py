from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.library.api_endpoints.CartItemCreate.serializers import \
    CartItemCreateSerializer
from apps.library.choices import CartStatus
from apps.library.models import Book, Cart, CartItem


class CartItemCreateApiView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemCreateSerializer
    queryset = CartItem.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            cart, created = Cart.objects.get_or_create(user=request.user, status=CartStatus.PENDING)
            cart_items = CartItem.objects.filter(cart=cart)
            book = Book.objects.get(id=request.data["book_id"])
            for item in cart_items:
                if item.book == book:
                    item.quantity += 1
                    item.save()
                    break
            else:
                CartItem.objects.create(cart=cart, book_id=request.data["book_id"])
            return Response({"result": "CartItem successfully created!"})
        except Exception as e:
            return Response({"error": f"{e}"})


__all__ = ["CartItemCreateApiView"]
