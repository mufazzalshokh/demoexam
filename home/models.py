from django.db import models


class NewsModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='title')
    image = models.FileField(upload_to='news')
    content = models.TextField(verbose_name='content')
    long_description = models.TextField(verbose_name='long_description')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'news'
