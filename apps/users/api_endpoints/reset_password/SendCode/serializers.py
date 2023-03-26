from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.users.models import CustomUser


class SendCodeSerializer(serializers.Serializer):
    phone_or_email = serializers.CharField(required=True)

    def validate(self, data):
        # get variables
        phone_or_email = data.get("phone_or_email", None)

        # check if user exists with given phone_or_email
        users = CustomUser.objects.filter(
            Q(phone_number=phone_or_email) |
            Q(email=phone_or_email)
        )
        if not users.exists():
            raise ValidationError({
                "phone_or_email": _("No user was found with this phone number/email")
            })

        data.update({'user': users.first()})
        return data
