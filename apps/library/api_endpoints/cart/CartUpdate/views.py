from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.library.api_endpoints.cart.CartUpdate.serializers import \
    CartUpdateSerializer
from apps.library.models import Cart


class CartUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartUpdateSerializer
    queryset = Cart.objects.all()


__all__ = ["CartUpdateView"]
