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
    """Модель всех фильмов """
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, verbose_name="Раздел")
    title = models.CharField(max_length=70, verbose_name="Название")
    image = models.ImageField(upload_to="images", verbose_name="Изображение")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(datetime.date.today().year)], verbose_name="Год"
    )
    country = models.CharField(max_length=70, verbose_name="Страна")
    director = models.CharField(max_length=70, verbose_name="Режисер")
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
    """Модель купона на скидку"""
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

    def value_percent(self):
        return str(self.value) + "%"

    def __str__(self):
        # return '{0} {1} %'.format(self.code, self.value)
        return self.code + " (" + str(self.value) + "%)"

    value_percent.short_description = "Размер скидки"


class Order(models.Model):
    """Модель скиндки"""
    need_delivery = models.BooleanField(verbose_name="Необходима доставка")
    discount = models.ForeignKey(Discount, verbose_name="Скидка", on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=70, verbose_name="Имя")
    phone = models.CharField(max_length=70, verbose_name="Телефон")
    email = models.EmailField()
    address = models.TextField(blank=True, verbose_name="Адрес")
    notice = models.CharField(max_length=150, verbose_name="Примечание к заказу", blank=True)
    data_order = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    data_send = models.DateTimeField(null=True, blank=True, verbose_name="Дата отправки")

    STATUSES = [
        ("NEW", "Новый заказ"),
        ("APR", "Подтвержден"),
        ("PAY", "Оплачен"),
        ("CNL", "Отменён"),
    ]

    status = models.CharField(choices=STATUSES, max_length=3, default="NEW", verbose_name="Статус")

    class Meta:
        ordering = ["-data_order"]
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return "ID: " + str(self.id)


class OrderLine(models.Model):
    """Модель заказа товара"""
    order = models.ForeignKey(Order, verbose_name="Заказ", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена", default=0)
    count = models.IntegerField(verbose_name="Колличество", validators=[MinValueValidator(1)], default=1)

    class Meta:
        verbose_name = "Строка заказа"
        verbose_name_plural = "Строки заказов"

    def __str__(self):
        return "Заказ (ID {0}) {1}: {2} шт" .format(self.order.id, self.product.title, self.count)


class Gallery(models.Model):
    photo_gallery = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фото галереи")
    # data_gallery = models.DateTimeField(auto_now_add=True, verbose_name="Дата о публикации фото")

    class Meta:
        verbose_name = "Фото галереи"
        verbose_name_plural = "Галерея"


class Comment(models.Model):
    commentary = models.TextField(verbose_name="Коментарий")
    data_order = models.DateTimeField(auto_now_add=True, verbose_name="Дата коментария")
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["data_order"]
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"

    def __str__(self):
        return self.title