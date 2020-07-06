from django.db import models

class Feedback(models.Model):
    name = models.CharField('От', max_length=255, blank=False, null=True)
    preview = models.ImageField('Картинка превью', upload_to='blog/', blank=False, null=True)
    page_title = models.CharField('Название страницы SEO', max_length=255, blank=True, null=True)
    page_description = models.TextField('Описание страницы SEO', blank=True, null=True)
    page_keywords = models.TextField('Keywords SEO', blank=True, null=True)
    content = models.TextField('Основной контент', blank=True, null=True)
    is_active = models.BooleanField('Отображать ?', default=True)

    def get_img(self):
        print(self.preview)
        if self.preview:
            return self.preview.url
        else:
            return ''


    def __str__(self):
        return f'Отзыв jn: {self.name}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"