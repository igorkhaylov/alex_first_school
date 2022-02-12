from modeltranslation.translator import register, TranslationOptions
from .models import MainBlock, News, Slider, Teachers, Questions


@register(MainBlock)
class MainBlockTranslationOptions(TranslationOptions):
    fields = ('about_school_text_1',
              'about_school_text_2',
              'history_of_school',
              )


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('text', )


@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle", "text")


@register(Teachers)
class TeachersTranslationOptions(TranslationOptions):
    fields = ("name", "description")


@register(Questions)
class QuestionsTranslationOptions(TranslationOptions):
    fields = ("question", "answer")

