from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.library.api_endpoints.OrderCreate.serializers import \
    OrderCreateSerializer
from apps.library.choices import CartStatus
from apps.library.models import Cart, Coupon, Order


class OrderCreateApiView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        coupon = Coupon.objects.get(id=request.data["coupon"])
        cart = Cart.objects.get(id=request.data["cart"])

        amount = cart.total * (100 + coupon.percent) / 100
        request.data["payment_amount"] = amount
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        cart.status = CartStatus.BOOKED
        cart.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


__all__ = ["OrderCreateApiView"]
