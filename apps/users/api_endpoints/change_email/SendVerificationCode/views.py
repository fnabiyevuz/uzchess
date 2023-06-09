from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.api_endpoints.change_email.SendVerificationCode.serializers import \
    SendVerificationCodeSerializer
from apps.users.permissions import IsRegisteredViaEmail
from apps.users.services.generators import generate_verification_code
from apps.users.services.message_senders import send_verification_code_email


class SendVerificationCodeAPIView(APIView):
    permission_classes = [IsRegisteredViaEmail]

    @swagger_auto_schema(request_body=SendVerificationCodeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = SendVerificationCodeSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)

        user = request.user
        new_email = serializer.validated_data["new_email"]

        if cache.get(user.id, None) is not None:
            # If phone number already exists in cache
            return Response(
                data={"error": "Verification code is already sent. Please wait for a while before continue"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # if phone number is available
        # generate code and store it in cache
        code = generate_verification_code()
        send_verification_code_email(new_email, code)

        cache_data = {
            "new_email": new_email,
            "code": code,
        }
        cache.set(user.id, cache_data, 120)

        return Response(data={"message": _("Verification code was sent successfully!")}, status=status.HTTP_200_OK)


__all__ = ["SendVerificationCodeAPIView"]
