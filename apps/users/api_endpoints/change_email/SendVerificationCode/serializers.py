from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.users.models import CustomUser


class SendVerificationCodeSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=8, max_length=128, required=True)
    new_email = serializers.EmailField(required=True)

    def validate(self, data):
        # check user's password is correct
        user = self.context['request'].user
        password = data['password']
        if not user.check_password(password):
            # if user's password is incorrect
            raise ValidationError({
                'password': _("Your password is incorrect!")
            })

        # check if new_phone_number is available
        if CustomUser.objects.filter(email=data['new_email']).exists():
            raise ValidationError({
                'new_email': _("This email is unavailable")
            })

        return data
