from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.library.api_endpoints.CartItemCreate.serializers import CartItemCreateSerializer
from apps.library.choices import PaymentStatus
from apps.library.models import Cart, CartItem


class CartCreateApiView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemCreateSerializer

    def create(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user, payment_status=PaymentStatus.PENDING)
        cart_item = CartItem.objects.create(cart=cart, book_id=request.data['book_id'])
        if cart and cart_item:
            return Response({'result': 'Cart and CartItem were successfully created!'})
        return Response({'error': 'Error at Cart or CartItem creating'})


__all__ = ["CartCreateApiView"]
