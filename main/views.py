from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import MainBlock, News, Slider, Teachers, Questions
from django.core.mail import send_mail


def index(request):
    main_block = MainBlock.objects.first()
    news = News.objects.all()[:3]
    sliders = Slider.objects.all()
    teachers = Teachers.objects.all()
    questions = Questions.objects.all()

    last_updated = News.objects.first()

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone_number = request.POST["phone"]
        text = request.POST["comment"]

        mes = "\tИмя отправителя: \n" + name + \
              "\n\n\tE-mail отправителя: \n" + email + \
              "\n\n\tНомер телефона: \n" + phone_number + \
              "\n\n\tСообщение: \n" + text
        print(mes)

        mail = send_mail('First-School', mes, 'totpravka@gmail.com',
                         ['igorkhaylov@yandex.com', ], fail_silently=False, )
        if mail:
            print("Сообщение успешно отправлено")
        else:
            print("Ошибка отправки сообщения")

        # print(request)
        # return HttpResponseRedirect()

        # return render(request, "main/contact-us.html")
        # return HttpResponseRedirect("/")
        return redirect("index")
    return render(request, "index.html", {"main_block": main_block,
                                          "news": news,
                                          "last_updated": last_updated,
                                          "sliders": sliders,
                                          "teachers": teachers,
                                          "questions": questions,
                                          })
