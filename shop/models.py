from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=70, help_text='Введите название раздела', blank=True, unique=True,
                             verbose_name="Название раздела")

    class Meta:
        ordering = ["id"]
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

    def __str__(self):
        return self.title
