from django.shortcuts import render
from .models import MainBlock, News, Slider, Teachers, Questions


def index(request):
    main_block = MainBlock.objects.first()
    news = News.objects.all()[:3]
    sliders = Slider.objects.all()
    teachers = Teachers.objects.all()
    questions = Questions.objects.all()

    last_updated = News.objects.first()
    return render(request, "index.html", {"main_block": main_block,
                                          "news": news,
                                          "last_updated": last_updated,
                                          "sliders": sliders,
                                          "teachers": teachers,
                                          "questions": questions,
                                          })
