from django.db import models
from pytils.translit import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
    name = models.CharField('Название статьи', max_length=255, blank=False, null=True)
    auto_slug = models.BooleanField('Создать ЧПУ ?', default=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True,editable=False)
    preview = models.ImageField('Картинка превью', upload_to='blog/', blank=False, null=True)
    main_img = models.ImageField('Картинка статьи', upload_to='blog/', blank=False, null=True)
    page_title = models.CharField('Название страницы SEO', max_length=255, blank=True, null=True)
    page_description = models.TextField('Описание страницы SEO', blank=True, null=True)
    page_keywords = models.TextField('Keywords SEO', blank=True, null=True)
    content = RichTextUploadingField('Основной контент', blank=True, null=True)
    is_active = models.BooleanField('Отображать ?', default=True)
    def save(self, *args, **kwargs):
        if self.auto_slug:
            self.name_slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return f'Статья: {self.name} ({self.name_slug})'

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


