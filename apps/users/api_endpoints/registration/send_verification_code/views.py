from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.api_endpoints.registration.send_verification_code.serializers import SendVerificationCodeSerializer
from apps.users.services.generators import generate_auth_session, generate_verification_code
from apps.users.services.message_senders import send_verification_code_sms, send_verification_code_email
from apps.users.choices import VIA_PHONE_NUMBER, VIA_EMAIL


class SendVerificationCodeAPIView(APIView):

    def post(self, request,  *args, **kwargs):
        serializer = SendVerificationCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        session = generate_auth_session()

        if data['auth_type'] is VIA_PHONE_NUMBER:
            # if user are registering VIA PHONE NUMBER
            phone_number = data['phone_number']
            if cache.get(phone_number, None) is not None:
                # If phone number already exists in cache
                return Response(
                    data={'error': 'Verification code is already sent. Please wait for a while before continue'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # if phone number is available
            code = generate_verification_code()
            send_verification_code_sms(phone_number, code)
            phone_data = {
                'session': session,
                'code': code,
            }
            cache.set(phone_number, phone_data, 120)
            data.update({'username': phone_number})

        if data['auth_type'] is VIA_EMAIL:
            # if user are registering VIA EMAIL
            email = data['email']
            if cache.get(email, None) is not None:
                # If phone number already exists in cache
                return Response(
                    data={'error': 'Verification code is already sent. Please wait for a while before continue'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # if phone number is available
            code = generate_verification_code()
            send_verification_code_email(email, code)
            email_data = {
                'session': session,
                'code': code,
            }
            cache.set(email, email_data, 120)
            data.update({'username': email})

        cache.set(session, data, 360)
        temp = cache.get(session)
        print(temp)
        print(data)
        print(type(data))
        data.update({'session': session})
        return Response(data=data, status=status.HTTP_200_OK)


__all__ = ['SendVerificationCodeAPIView']
