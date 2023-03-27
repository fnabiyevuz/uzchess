from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.library.models import Cart
from apps.users.api_endpoints.profile.GetOrders.serializers import \
    GetOrdersListSerializer


class GetOrdersListAPIView(ListAPIView):
    serializer_class = GetOrdersListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Get orders queryset that were ordered by request user
        """
        orders = Cart.objects.filter(user=self.request.user)
        self.queryset = orders

        return orders


__all__ = ["GetOrdersListAPIView"]
