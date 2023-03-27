from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedModel


class Info(TimeStampedModel):
    working_time = models.CharField(verbose_name=_("Working time"), max_length=255)
    email = models.EmailField(verbose_name=_("Email"))
    phone = PhoneNumberField(region="UZ", verbose_name=_("Phone number"))
    metro = models.CharField(verbose_name=_("Metro"), max_length=255)
    map = models.TextField(verbose_name=_("Map"))

    def __str__(self):
        return self.working_time

    class Meta:
        verbose_name = "Info"
        verbose_name_plural = "Infos"


class Feedback(TimeStampedModel):
    full_name = models.CharField(verbose_name=_("Full name"), max_length=255, null=True, blank=True)
    phone = PhoneNumberField(region="UZ", verbose_name=_("Phone number"))
    text = models.TextField(verbose_name=_("Text"))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"


class RulesOfUsing(TimeStampedModel):
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    content = models.TextField(verbose_name=_("Content"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Rules Of Using"
        verbose_name_plural = "Rules Of Usings"
