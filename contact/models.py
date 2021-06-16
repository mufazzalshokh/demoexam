from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='email')
    comment = models.TextField(verbose_name='comment')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    def __str__(self):
        return self.name


class Meta:
    verbose_name = 'contact'
    verbose_name_plural = 'contacts'
