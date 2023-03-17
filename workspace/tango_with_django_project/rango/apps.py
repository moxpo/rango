from django.apps import AppConfig

from django.contrib import admin
from rango.models import Category, Page


class RangoConfig(AppConfig):
    name = 'rango'


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'views')
    ordering = ('title',)

admin.site.register(Category)
admin.site.register(Page, PageAdmin)