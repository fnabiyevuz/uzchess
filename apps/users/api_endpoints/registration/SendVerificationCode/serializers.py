from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.users.choices import VIA_EMAIL, VIA_PHONE_NUMBER
from apps.users.models import CustomUser


class SendVerificationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "full_name",
            "phone_number",
            "email",
        )
        ref_name = "SendVerificationCodeRegistrationSerializer"

    def validate(self, data):
        # get variables
        phone_number = data.get("phone_number", None)
        email = data.get("email", None)

        # check if user sent only one of phone number and email
        if phone_number is not None:
            if email is not None:
                # if both of phone number and email is entered
                raise ValidationError(
                    {
                        "error": _("You can enter only one of phone number and email at a time!"),
                    }
                )

            # if only phone number is entered
            # check phone number is available
            if not CustomUser.is_phone_number_available(phone_number):
                raise ValidationError({"phone_number": _("This number is already taken")})
            data.update({"auth_type": VIA_PHONE_NUMBER})
            return data

        if email is not None:
            # if only email is entered
            # check email is available
            if not CustomUser.is_email_available(email):
                raise ValidationError({"email": _("This email is already taken")})
            data.update({"auth_type": VIA_EMAIL})
            return data

        # if none of phone number and email is entered
        raise ValidationError(
            {
                "error": _("You must enter phone number or email!"),
            }
        )
