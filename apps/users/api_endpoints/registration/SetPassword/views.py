from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from apps.users.api_endpoints.registration.SetPassword.serializers import \
    SetPasswordSerializer
from apps.users.models import CustomUser


class SetPasswordAPIView(APIView):

    @swagger_auto_schema(request_body=SetPasswordSerializer)
    def post(self, request, *arg, **kwargs):
        serializer = SetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # get values from request data
        session = serializer.validated_data["session"]
        password = serializer.validated_data["password"]

        session_data = cache.get(session, None)

        if session_data is None:
            # if nothing found with given session
            return Response(data={"error": _("Invalid session!")}, status=status.HTTP_400_BAD_REQUEST)

        # check user is verified with this session
        is_verified = session_data.pop("is_verified", None)
        if is_verified is None:
            # if user is not verified
            return Response(
                data={"error": _("User is not verified with this session!")}, status=status.HTTP_400_BAD_REQUEST
            )

        # if everything is OKAY
        user = CustomUser(**session_data)
        user.set_password(password)
        user.save()

        # create token for this user
        session_data.update(user.get_tokens())

        return Response(data=session_data, status=status.HTTP_201_CREATED)


__all__ = ["SetPasswordAPIView"]
