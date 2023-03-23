from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedModel
from apps.users.choices import AUTH_TYPES


# Create your models here.
class CustomUser(AbstractUser, TimeStampedModel):
    first_name = None
    last_name = None
    full_name = models.CharField(max_length=100, verbose_name=_("full name"))
    birth_date = models.DateTimeField(verbose_name=_("date of birth"), null=True, blank=True)
    email = models.EmailField(verbose_name=_("email address"), null=True, blank=True)
    phone_number = PhoneNumberField(region='UZ', verbose_name=_("phone number"), null=True, blank=True)
    auth_type = models.CharField(max_length=3, choices=AUTH_TYPES)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.username

    @classmethod
    def is_phone_number_available(cls, phone_number):
        if cls.objects.filter(phone_number=phone_number).exists():
            return False
        return True

    @classmethod
    def is_email_available(cls, email):
        if cls.objects.filter(email=email).exists():
            return False
        return True


class TestModel(models.Model):
    test_field = models.CharField(max_length=100, verbose_name=_("test name"), blank=True, null=True)

