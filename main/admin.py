from django.contrib import admin
from .models import MainBlock
from modeltranslation.admin import TranslationAdmin


@admin.register(MainBlock)
class MainBlockAdmin(TranslationAdmin):
    list_display = ("display", )
    readonly_fields = ("display", )
