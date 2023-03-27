from rest_framework import serializers

from apps.course.models import Certificate, Course


class GenerateCertificateSerializer(serializers.Serializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    full_name = serializers.CharField(max_length=255, required=False)


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ("id", "course", "user", "cid", "full_name", "file", "created_at", "updated_at")
