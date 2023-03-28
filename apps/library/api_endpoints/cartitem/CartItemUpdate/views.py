from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.library.api_endpoints.cartitem.CartItemUpdate.serializers import \
    CartItemUpdateSerializer
from apps.library.models import CartItem


class CartItemUpdateApiView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemUpdateSerializer
    queryset = CartItem.objects.all()


__all__ = ["CartItemUpdateApiView"]
