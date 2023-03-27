from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.library.api_endpoints.CartItemUpdate.serializers import \
    CartItemUpdateSerializer
from apps.library.models import CartItem


class CartItemCreateApiView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemUpdateSerializer
    queryset = CartItem.objects.all()


__all__ = ["CartItemCreateApiView"]
