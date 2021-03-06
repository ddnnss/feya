# Generated by Django 3.0.7 on 2020-06-11 18:33

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название страницы')),
                ('name_slug', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание категории')),
                ('page_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название страницы SEO')),
                ('page_description', models.TextField(blank=True, null=True, verbose_name='Описание страницы SEO')),
                ('page_keywords', models.TextField(blank=True, null=True, verbose_name='Keywords SEO')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
    ]
