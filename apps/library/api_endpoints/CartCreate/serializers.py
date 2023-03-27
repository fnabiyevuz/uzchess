from rest_framework.serializers import ModelSerializer

from apps.library.models import Cart


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user')