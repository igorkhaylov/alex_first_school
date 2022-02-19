from django.contrib import admin
from .models import MainBlock, News, Slider, Teachers, Questions
from modeltranslation.admin import TranslationAdmin


@admin.register(MainBlock)
class MainBlockAdmin(TranslationAdmin):
    list_display = ("display", )
    readonly_fields = ("display", )


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ("title", )
    # readonly_fields = ("date_created", )

    save_as = True


@admin.register(Slider)
class SliderAdmin(TranslationAdmin):
    list_display = ("title", )

    save_as = True


@admin.register(Teachers)
class TeachersAdmin(TranslationAdmin):
    list_display = ("name", )

    # save_as = True


@admin.register(Questions)
class QuestionsAdmin(TranslationAdmin):
    list_display = ("question", )


admin.site.site_title = "Управление сайтом"
admin.site.site_header = "Школа №1"
