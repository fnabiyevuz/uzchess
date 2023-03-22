from django.contrib import admin
# from modeltranslation.admin import TranslationAdmin

from apps.users.models import CustomUser, TestModel


# class UserAdmin(TranslationAdmin):
#     pass


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(TestModel)
