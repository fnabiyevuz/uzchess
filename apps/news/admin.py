from django.contrib import admin

from apps.news.models import News, NewsView


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "photo")
    list_display_links = ("id", "title")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(NewsView)
class NewsViewAdmin(admin.ModelAdmin):
    list_display = ("id", "news", "user", "device_id")
    list_display_links = ("id", "news")
