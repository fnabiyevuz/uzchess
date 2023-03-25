from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.api_endpoints.change_phone_number.VerifyCode.serializers import VerifyCodeSerializer


class VerifyCodeAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = VerifyCodeSerializer(data=request)
        serializer.is_valid(raise_exception=True)

        # get variables
        user = request.user
        given_code = serializer.validated_data['code']
        cache_data = cache.get(user.id, None)

        if cache_data is None:
            # if NO cached data for this user found
            return Response(
                data={'error': _("Verification code is expired!")},
                status=status.HTTP_400_BAD_REQUEST
            )

        # check if given code is correct
        if given_code == cache_data['code']:
            user.phone_number = cache_data['new_phone_number']
            user.username = user.phone_number
            user.save()

        return Response(
            data={'message': _("Your phone number changed successfully")},
            status=status.HTTP_200_OK
        )


__all__ = ['VerifyCodeAPIView']
