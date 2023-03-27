from rest_framework import serializers


class VerifyCodeSerializer(serializers.Serializer):
    phone_or_email = serializers.CharField(required=True)
    code = serializers.CharField(required=True)
    session = serializers.CharField(max_length=32, required=True)

    class Meta:
        ref_name = 'VerifyCodeResetPasswordSerializer'
