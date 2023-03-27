from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.api_endpoints.profile.GetOrders.serializers import GetOrdersListSerializer
from apps.library.models import Cart


class GetOrdersListAPIView(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = GetOrdersListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Get orders queryset that were ordered by request user
        """
        if not self.request:
            return Cart.objects.none()

        orders = Cart.objects.filter(user=self.request.user)

        return orders


__all__ = ['GetOrdersListAPIView']
