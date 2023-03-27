from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from apps.users.api_endpoints.reset_password.SendCode.serializers import SendCodeSerializer
from apps.users.services.generators import generate_auth_session, generate_verification_code
from apps.users.services.message_senders import send_verification_code_email, send_verification_code_sms
from apps.users.choices import VIA_EMAIL, VIA_PHONE_NUMBER


class SendCodeAPIView(APIView):

    @swagger_auto_schema(request_body=SendCodeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = SendCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        phone_or_email = serializer.validated_data['phone_or_email']

        # check if reset password code is already sent or not
        if cache.get(phone_or_email, None) is not None:
            # if code is already sent
            return Response(
                data={'error': _("Code is already sent. Please, wait a while before continue")},
                status=status.HTTP_400_BAD_REQUEST
            )

        # generate session and code
        session = generate_auth_session()
        code = generate_verification_code()

        if user.auth_type == VIA_PHONE_NUMBER:
            # if user is registered via Phone Number
            send_verification_code_sms(user.phone_number, code)

        if user.auth_type == VIA_EMAIL:
            # if user is registered via Email
            send_verification_code_email(user.email, code)

        phone_or_email_data = {
            'session': session,
            'code': code,
        }

        # save data to cache
        cache.set(phone_or_email, phone_or_email_data, 120)
        cache.set(session, {'user_id': user.id}, 600)

        return Response(
            data={'session': session},
            status=status.HTTP_200_OK
        )


__all__ = ['SendCodeAPIView']
