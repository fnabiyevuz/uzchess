from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.api_endpoints.change_email.VerifyCode.serializers import VerifyCodeSerializer
from apps.users.permissions import IsRegisteredViaEmail


class VerifyCodeAPIView(APIView):
    permission_classes = [IsRegisteredViaEmail]

    def post(self, request, *args, **kwargs):
        serializer = VerifyCodeSerializer(data=request.data)
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
        if given_code != cache_data['code']:
            # if given code is incorrect
            return Response(
                data={'message': _("Your verification code is incorrect!")},
                status=status.HTTP_400_BAD_REQUEST
            )

        # if given code is correctYour phone number changed successfully
        user.email = cache_data['new_email']
        user.username = user.email
        user.save()

        return Response(
            data={'message': _("Your email changed successfully")},
            status=status.HTTP_200_OK
        )


__all__ = ['VerifyCodeAPIView']
