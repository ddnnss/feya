from django.db import models
from pytils.translit import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class EventPage(models.Model):
    name = models.CharField('Название страницы', max_length=255, blank=False, null=True)
    auto_slug = models.BooleanField('Создать ЧПУ ?', default=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextUploadingField('Основной контент', blank=True, null=True)
    page_title = models.CharField('Название страницы SEO', max_length=255, blank=True, null=True)
    page_description = models.TextField('Описание страницы SEO', blank=True, null=True)
    page_keywords = models.TextField('Keywords SEO', blank=True, null=True)


    def save(self, *args, **kwargs):
        if self.auto_slug:
            self.name_slug = slugify(self.name)
        super(EventPage, self).save(*args, **kwargs)

    def __str__(self):
        return f'Мероприятие : {self.name} ({self.name_slug})'

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
