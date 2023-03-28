from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.api_endpoints.profile.UpdateProfile.serializers import \
    UpdateProfileSerializer


class UpdateProfileAPIView(UpdateAPIView):
    serializer_class = UpdateProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


__all__ = ["UpdateProfileAPIView"]
