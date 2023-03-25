from rest_framework.generics import UpdateAPIView

from apps.users.api_endpoints.profile.GetProfile.serializers import GetProfileSerializer


class GetProfileAPIView(UpdateAPIView):
    serializer_class = GetProfileSerializer

    def get_object(self):
        return self.request.user


__all__ = ['GetProfileAPIView']
