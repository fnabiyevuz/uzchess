from django.core.cache import cache
from django.utils.translation import gettext_lazy as _

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.api_endpoints.registration.verify_code.serializers import VerifyCodeSerializer


class VerifyCodeAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = VerifyCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # get values from request data
        phone_or_email = serializer.validated_data['phone_or_email']
        session = serializer.validated_data['session']
        code = serializer.validated_data['code']

        cache_data = cache.get(phone_or_email, None)

        if cache_data is None:
            # if nothing is found with given phone number or email
            return Response(
                data={'error': _("Verification code is expired. Or invalid phone/email entered!")},
                status=status.HTTP_400_BAD_REQUEST
            )

        if cache_data['code'] != code:
            # if incorrect code is entered
            return Response(
                data={'error': _("Incorrect Code!")}
            )

        # if everything is OKAY
        # set is_verified TRUE for this user's session
        session_cache_data = cache.get(session, None)
        session_cache_data.update({'is_verified': True})
        cache.set(session, session_cache_data)

        # return response
        return Response(
            data={'message': _("Your verification completed successfully!")},
            status=status.HTTP_200_OK
        )


__all__ = ['VerifyCodeAPIView']
