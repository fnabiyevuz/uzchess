from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        # get user's auth token and delete it
        token = Token.objects.filter(user=request.user)
        token.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
