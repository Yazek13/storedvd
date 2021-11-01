import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=70, help_text='Введите название раздела', unique=True,
                             verbose_name="Название раздела")

    class Meta:
        ordering = ["id"]
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

    def __str__(self):
        return self.title


class Product(models.Model):
    section = models.ForeignKey("Section", on_delete=models.SET_NULL, null=True, verbose_name="Раздел")
    title = models.CharField(max_length=70, verbose_name="Название")
    image = models.ImageField(upload_to="images", verbose_name="Изображение")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(datetime.date.today().year)], verbose_name="Год"
    )
    country = models.CharField(max_length=70, verbose_name="Страна")
    director = country = models.CharField(max_length=70, verbose_name="Режисер")
    play = models.IntegerField(null=True, verbose_name="Продолжительность фильма",
                               validators=[MinValueValidator(1)],
                               blank=True, help_text="В секундах")
    cast = models.TextField(verbose_name="В ролях")
    discription = models.TextField(verbose_name="Описание фильма")
    date = models.DateField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        ordering = ["title", "-year"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return '{0} [{1}]'.format(self.title, self.section.title)


class Discount(models.Model):
    code = models.CharField(max_length=10, verbose_name="Код купона")
    value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        verbose_name="Размер скидки",
        help_text="В процентах"
    )

    class Meta:
        ordering = ["-value"]
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"

    def __str__(self):
        # return '{0} {1} %'.format(self.code, self.value)
        return self.code + " (" + str(self.value) + "%)"
