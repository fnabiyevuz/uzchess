from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class SetPasswordSerializer(serializers.Serializer):
    session = serializers.CharField(max_length=32)
    password = serializers.CharField(min_length=8, max_length=128, required=True)
    password2 = serializers.CharField(min_length=8, max_length=128, required=True)

    def validate(self, data):

        # check both passwords are the same
        if data['password'] != data['password2']:
            # if passwords are different
            raise ValidationError({
                'error': _("Passwords does not match!")
            })

        return data
