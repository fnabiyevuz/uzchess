from django.http import Http404
from django.utils.crypto import get_random_string
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.library.api_endpoints.CartUpdate.serializers import CartUpdateSerializer
from apps.library.models import Cart


class CartUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartUpdateSerializer

    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        cart = self.get_object(pk)
        cart.full_name = request.data["full_name"]
        cart.phone = request.data["phone"]
        cart.email = request.data["email"]
        cart.coupon_id = request.data["coupon"]
        cart.order_id = get_random_string(length=1, allowed_chars="0123456789")
        cart.save()
        serializer = self.serializer_class(cart).data

        return Response(serializer)


__all__ = ['CartUpdateView']