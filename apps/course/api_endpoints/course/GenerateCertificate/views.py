from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.course.models import Certificate, UserCourse
from apps.course.utils import generate_certificate

from .serializers import CertificateSerializer, GenerateCertificateSerializer


class GenerateCertificateAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GenerateCertificateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        course = serializer.validated_data["course"]
        full_name = serializer.validated_data["full_name"]
        print('kourse', course, full_name)
        if Certificate.objects.filter(course=course, user=request.user).exists():
            data = CertificateSerializer(
                Certificate.objects.get(course=course, user=request.user), context={"request": request}
            ).data
            return Response(data=data, status=status.HTTP_200_OK)
        user_course = UserCourse.objects.get(user=request.user, course=course)

        if not user_course.is_finished:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        certificate = generate_certificate(user_course, full_name)
        return Response(
            data=CertificateSerializer(certificate, context={"request": request}).data, status=status.HTTP_201_CREATED
        )
