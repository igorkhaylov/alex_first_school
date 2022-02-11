from django.db import models


class MainBlock(models.Model):
    display = models.CharField(max_length=120, default="Главная", null=True)
    about_school_text_1 = models.TextField(null=True)
    about_school_picture_1 = models.ImageField(upload_to="about_school/", null=True)
    about_school_text_2 = models.TextField(null=True)
    about_school_picture_2 = models.ImageField(upload_to="about_school/", null=True)
    history_of_school = models.TextField(max_length=500, null=True)


