from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.api_endpoints.reset_password.ResetPassword.serializers import \
    ResetPasswordSerializer
from apps.users.models import CustomUser


class ResetPasswordAPIView(APIView):
    @swagger_auto_schema(request_body=ResetPasswordSerializer)
    def post(self, request, *arg, **kwargs):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # get values from request data
        session = serializer.validated_data["session"]
        password = serializer.validated_data["password"]

        session_data = cache.get(session, None)

        if session_data is None:
            # if nothing found with given session
            return Response(data={"error": _("Invalid session!")}, status=status.HTTP_400_BAD_REQUEST)

        # check user is verified with this session
        is_verified = session_data.get("is_verified", None)
        if is_verified is None:
            # if user is not verified
            return Response(
                data={"error": _("User is not verified with this session!")}, status=status.HTTP_400_BAD_REQUEST
            )

        # if everything is OKAY
        user = get_object_or_404(CustomUser.objects.all(), id=session_data["user_id"])
        user.set_password(password)
        user.save()

        return Response(data={"message": _("Reset password successfully")}, status=status.HTTP_200_OK)


__all__ = ["ResetPasswordAPIView"]
