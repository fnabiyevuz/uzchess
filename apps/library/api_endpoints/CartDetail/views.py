from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.library.api_endpoints.CartDetail.serializers import \
    CartDetailSerializer
from apps.library.models import Cart


class CartDetailApiView(RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartDetailSerializer
    permission_classes = [IsAuthenticated]


__all__ = ["CartDetailApiView"]
