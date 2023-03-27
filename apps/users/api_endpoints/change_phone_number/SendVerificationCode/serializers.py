from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from phonenumber_field.serializerfields import PhoneNumberField

from apps.users.models import CustomUser


class SendVerificationCodeSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=8, max_length=128, required=True)
    new_phone_number = PhoneNumberField(region="UZ", required=True)

    class Meta:
        ref_name = 'SendVerificationCodePhoneSerializer'

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
        if CustomUser.objects.filter(phone_number=data['new_phone_number']).exists():
            raise ValidationError({
                'new_phone_number': _("This phone number is unavailable")
            })

        return data
