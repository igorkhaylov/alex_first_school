from django.db import models


class MainBlock(models.Model):
    display = models.CharField(max_length=120, default="Главная", null=True)
    about_school_text_1 = models.TextField(null=True)
    about_school_picture_1 = models.ImageField(upload_to="about_school/", null=True)
    about_school_text_2 = models.TextField(null=True)
    about_school_picture_2 = models.ImageField(upload_to="about_school/", null=True)
    history_of_school = models.TextField(max_length=500, null=True)
    slider_picture = models.ImageField(upload_to="slider_picture", null=True)

    student_counter = models.SmallIntegerField(default=0, null=True)
    teacher_counter = models.SmallIntegerField(default=0, null=True)
    cabinet_counter = models.SmallIntegerField(default=0, null=True)
    program_counter = models.SmallIntegerField(default=0, null=True)

    def __str__(self):
        return self.display

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главная"


class News(models.Model):
    title = models.CharField(max_length=120, null=True)
    picture = models.ImageField(upload_to="news/", null=True)
    text = models.TextField(max_length=210, null=True, )
    date_created = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-id", ]


class Slider(models.Model):
    title = models.CharField(max_length=60, null=True)
    subtitle = models.CharField(max_length=120, null=True, blank=True)
    text = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"
        ordering = ["-id"]


class Teachers(models.Model):
    name = models.CharField(max_length=120, null=True)
    description = models.CharField(max_length=250, null=True)
    picture = models.ImageField(upload_to="teachers/", null=True)
    level = models.SmallIntegerField(default=0, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
        ordering = ["-level", ]


class Questions(models.Model):
    question = models.CharField(max_length=250, null=True)
    answer = models.TextField(max_length=1500, null=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ["-id"]






