from django.contrib import admin

from apps.main.models import Info, Feedback, RulesOfUsing


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'working_time', 'email', 'phone', 'metro', 'map')
    list_display_links = ('id', 'working_time')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'text')
    list_display_links = ('id', 'full_name')


@admin.register(RulesOfUsing)
class RulesOfUsingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    list_display_links = ('id', 'title')
