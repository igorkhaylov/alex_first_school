# Generated by Django 4.0.2 on 2022-02-12 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_mainblock_slider_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, null=True)),
                ('title_ru', models.CharField(max_length=60, null=True)),
                ('title_uz', models.CharField(max_length=60, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=120, null=True)),
                ('subtitle_ru', models.CharField(blank=True, max_length=120, null=True)),
                ('subtitle_uz', models.CharField(blank=True, max_length=120, null=True)),
                ('text', models.TextField(max_length=500)),
                ('text_ru', models.TextField(max_length=500, null=True)),
                ('text_uz', models.TextField(max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдеры',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterModelOptions(
            name='mainblock',
            options={'verbose_name': 'Главная', 'verbose_name_plural': 'Главная'},
        ),
    ]
