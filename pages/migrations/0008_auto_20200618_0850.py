# Generated by Django 2.2.7 on 2020-06-18 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_topmenuitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topmenuitem',
            name='icon',
        ),
        migrations.AddField(
            model_name='topmenuitem',
            name='banner_bg',
            field=models.ImageField(null=True, upload_to='banner/', verbose_name='Картинка баннера'),
        ),
    ]
