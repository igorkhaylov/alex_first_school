# Generated by Django 4.0.2 on 2022-02-12 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_teachers_alter_slider_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250, null=True)),
                ('question_ru', models.CharField(max_length=250, null=True)),
                ('question_uz', models.CharField(max_length=250, null=True)),
                ('answer', models.TextField(max_length=1500, null=True)),
                ('answer_ru', models.TextField(max_length=1500, null=True)),
                ('answer_uz', models.TextField(max_length=1500, null=True)),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['-id'],
            },
        ),
    ]
