from django.db import models


class Product(models.Model):
    name = models.CharField('Название товара', max_length=255, blank=True)
    brand = models.CharField('Бренд', max_length=255, blank=True)
    article = models.CharField('Артикул', max_length=32, blank=True)
    rating = models.PositiveSmallIntegerField(
        'Рейтинг товара',
        default=0,
        null=True,
        blank=True
    )
    actual_price = models.CharField('Цена', max_length=32, blank=True)
    composition = models.TextField('Состав', default='', blank=True)
    description = models.TextField('Описание товара', default='', blank=True)
    params = models.TextField('Характеристики товара', default='', blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.brand)