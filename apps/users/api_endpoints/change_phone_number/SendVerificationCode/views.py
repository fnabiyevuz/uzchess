from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.api_endpoints.change_phone_number.SendVerificationCode.serializers import SendVerificationCodeSerializer
from apps.users.services.generators import generate_verification_code
from apps.users.services.message_senders import send_verification_code_sms


class SendVerificationCodeAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = SendVerificationCodeSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = request.user
        new_phone_number = serializer.validated_data['new_phone_number']

        if cache.get(new_phone_number, None) is not None:
            # If phone number already exists in cache
            return Response(
                data={"error": "Verification code is already sent. Please wait for a while before continue"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # if phone number is available
        # generate code and store it in cache
        code = generate_verification_code()
        send_verification_code_sms(new_phone_number, code)

        cache_data = {
            "new_phone_number": new_phone_number,
            "code": code,
        }
        cache.set(user.id, cache_data, 120)

        return Response(
            data={'message': _("Verification code was sent successfully!")},
            status=status.HTTP_200_OK
        )


__all__ = ['SendVerificationCodeAPIView']
