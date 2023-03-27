from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=8, max_length=128, required=True)
    new_password = serializers.CharField(min_length=8, max_length=128, required=True)
    new_password2 = serializers.CharField(min_length=8, max_length=128, required=True)

    def validate(self, data):
        # check user's password is correct
        user = self.context["request"].user
        password = data["password"]
        if not user.check_password(password):
            # if user's password is incorrect
            raise ValidationError({"password": _("Your password is incorrect!")})

        # check both passwords are the same
        if data["new_password"] != data["new_password2"]:
            # if passwords are different
            raise ValidationError({"error": _("Passwords does not match!")})

        return data
