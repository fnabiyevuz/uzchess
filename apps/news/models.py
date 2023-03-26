from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import ForeignKey, CharField, SlugField, ImageField, CASCADE
from django.utils.translation import gettext as _

from apps.common.models import TimeStampedModel
from apps.users.models import CustomUser


class News(TimeStampedModel):
    title = CharField(_('Title'), max_length=255)
    slug = SlugField(_('Slug'), unique=True)
    photo = ImageField(_('Photo'), upload_to='news/%Y/%m/%d/')
    context = RichTextField(_('Context'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']


class NewsView(TimeStampedModel):
    device_id = models.CharField(max_length=100, verbose_name=_('Device ID'))
    news = ForeignKey(News, on_delete=CASCADE, verbose_name=_('News'))
    user = models.ForeignKey(CustomUser, verbose_name=_('User'), on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.device_id
