from rest_framework.generics import UpdateAPIView

from apps.users.api_endpoints.profile.UpdateProfile.serializers import UpdateProfileSerializer


class UpdateProfileAPIView(UpdateAPIView):
    serializer_class = UpdateProfileSerializer

    def get_object(self):
        return self.request.user


__all__ = ['UpdateProfileAPIView']
