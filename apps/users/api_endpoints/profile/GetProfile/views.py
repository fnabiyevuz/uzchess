from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.api_endpoints.profile.GetProfile.serializers import \
    GetProfileSerializer


class GetProfileAPIView(RetrieveAPIView):
    serializer_class = GetProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


__all__ = ["GetProfileAPIView"]
