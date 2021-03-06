# Generated by Django 3.0.7 on 2020-06-11 20:06

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='auto_slug',
            field=models.BooleanField(default=True, verbose_name='Создать ЧПУ ?'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Основной контент'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='name_slug',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
