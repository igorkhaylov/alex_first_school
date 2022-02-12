# Generated by Django 4.0.2 on 2022-02-11 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.CharField(default='Главная', max_length=120, null=True)),
                ('about_school_text_1', models.TextField(null=True)),
                ('about_school_text_1_ru', models.TextField(null=True)),
                ('about_school_text_1_uz', models.TextField(null=True)),
                ('about_school_picture_1', models.ImageField(null=True, upload_to='about_school/')),
                ('about_school_text_2', models.TextField(null=True)),
                ('about_school_text_2_ru', models.TextField(null=True)),
                ('about_school_text_2_uz', models.TextField(null=True)),
                ('about_school_picture_2', models.ImageField(null=True, upload_to='about_school/')),
                ('history_of_school', models.TextField(max_length=500, null=True)),
                ('history_of_school_ru', models.TextField(max_length=500, null=True)),
                ('history_of_school_uz', models.TextField(max_length=500, null=True)),
            ],
        ),
    ]