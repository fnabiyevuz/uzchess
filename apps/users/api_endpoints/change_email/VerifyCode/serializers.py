from rest_framework import serializers


class VerifyCodeSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)