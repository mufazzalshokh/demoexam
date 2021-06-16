from django.db import models


class DetailNewsModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='title')
    content = models.TextField(verbose_name='content')
