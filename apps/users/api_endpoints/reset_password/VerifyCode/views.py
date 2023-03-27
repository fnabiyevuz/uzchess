from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from apps.users.api_endpoints.reset_password.VerifyCode.serializers \
    import VerifyCodeSerializer


class VerifyCodeAPIView(APIView):

    @swagger_auto_schema(request_body=VerifyCodeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = VerifyCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # get variables
        phone_or_email = serializer.validated_data['phone_or_email']
        code = serializer.validated_data['code']
        session = serializer.validated_data['session']

        # check verification code exists for this phone or email in cache
        cache_data = cache.get(phone_or_email, None)
        if cache_data is None:
            # if nothing found in cache
            return Response(
                data={'error': _("Code is expired or Incorrect phone number/email was entered")},
                status=status.HTTP_400_BAD_REQUEST
            )

        # check if code is correct
        if code != cache_data['code']:
            # if incorrect code entered
            return Response(
                data={'error': _("Incorrect code!")},
                status=status.HTTP_400_BAD_REQUEST
            )

        # get session cache data, modify it and save again to cache
        session_data = cache.get(session, None)
        session_data.update({'is_verified': True})
        cache.set(session, session_data, 600)

        return Response(
            data={'message': _("Confirmed successfully!")},
            status=status.HTTP_200_OK
        )


__all__ = ['VerifyCodeAPIView']
