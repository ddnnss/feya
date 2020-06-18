from django.db import models
from pytils.translit import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from events_content.models import EventPage


class StaticPage(models.Model):
    name = models.CharField('Название страницы', max_length=255, blank=False, null=True)
    auto_slug = models.BooleanField('Создать ЧПУ ?', default=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    is_home_page = models.BooleanField('Главная страница ?', default=False)
    content = RichTextUploadingField('Основной контент', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.auto_slug:
            self.name_slug = slugify(self.name)
        super(StaticPage, self).save(*args, **kwargs)

    def __str__(self):
        return f'Статичесткая страница: {self.name} ({self.name_slug})'

    class Meta:
        verbose_name = "Статическая страница"
        verbose_name_plural = "Статические страницы"

class TopMenuItem(models.Model):
    banner_bg = models.ImageField('Картинка баннера',upload_to='banner/', blank=False, null=True)
    name = models.CharField('Название пункта', max_length=255, blank=False, null=True)
    event_url = models.ForeignKey(EventPage, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name='Ссылка на мероприятие')
    custom_url = models.CharField('Ссылка(без указания домена)', max_length=100, blank=True, null=True)
    is_active = models.BooleanField('Отображать ?', default=True)

    def __str__(self):
        return f'Пункт верхнего меню: {self.name}'

    class Meta:
        verbose_name = "Пункт верхнего меню"
        verbose_name_plural = "Пункты верхнего меню"

class LeftMenuItem(models.Model):
    icon = models.ImageField('Иконка',upload_to='menu_icons/', blank=False, null=True)
    event_url = models.ForeignKey(EventPage, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name='Ссылка на мероприятие')
    custom_url = models.CharField('Ссылка(без указания домена)', max_length=100, blank=True, null=True)
    is_active = models.BooleanField('Отображать ?', default=True)

    def __str__(self):
        return f'Пункт левого меню: {self.event_url.name}'

    class Meta:
        verbose_name = "Пункт левого меню"
        verbose_name_plural = "Пункты левого меню"

class RightMenuItem(models.Model):
    name = models.CharField('Название пункта (указывать если используется Ссылка(без указания домена))', max_length=255, blank=True, null=True)
    static_url = models.ForeignKey(StaticPage, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name='Ссылка на статическую страницу')
    custom_url = models.CharField('Ссылка(без указания домена)', max_length=100, blank=True, null=True)
    is_callback = models.BooleanField('Кнопка заказать звонок ?', default=False)
    is_active = models.BooleanField('Отображать ?', default=True)

    def __str__(self):
        if not self.is_callback:
            if self.static_url:
                return f'Пункт правого меню: {self.static_url.name}'
            else:
                return f'Пункт правого меню: {self.name}'
        else:
            return f'Пункт правого меню: заказать звонок'

    class Meta:
        verbose_name = "Пункт правого меню"
        verbose_name_plural = "Пункты правого меню"