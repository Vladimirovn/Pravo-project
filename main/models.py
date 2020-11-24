from django.db import models

# Create your models here.

from django.db.models import Model


class Review(Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return f" Отзыв {self.title}"


    class Meta:
        ordering = ['order']
