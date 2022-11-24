from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Назва', max_length=50)
    task = models.TextField('Опис', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'