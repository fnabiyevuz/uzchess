from django.utils.translation import gettext_lazy as _
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.api_endpoints.profile.ChangePassword.serializers import ChangePasswordSerializer


class ChangePasswordAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        # get user
        user = request.user

        # set new password
        user.set_password(serializer.validated_data['new_password'])
        user.save()

        return Response(
            data={'message': _("You changed your password successfully!")},
            status=status.HTTP_200_OK
        )


__all__ = ['ChangePasswordAPIView']
