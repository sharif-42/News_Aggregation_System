from django.contrib import admin

from .models import News


@admin.register(News)
class BanglaNewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'news_type',
        'headline',
        'url',
        'news_category',
        'author',
        'summary',
    )
    list_filter = ('published_time',)