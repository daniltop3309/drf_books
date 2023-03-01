from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    annotation = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
