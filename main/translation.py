from modeltranslation.translator import register, TranslationOptions
from .models import MainBlock


@register(MainBlock)
class MainBlockTranslationOptions(TranslationOptions):
    fields = ('about_school_text_1',
              'about_school_text_2',
              'history_of_school',
              )
