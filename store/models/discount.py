from django.db import models
from .product import Products

from django.core.validators import MinValueValidator, MaxValueValidator


class Discount(models.Model):
    name = models.CharField(max_length=40, help_text="Максимальное значение 40", verbose_name='Название акции')
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                   help_text="Значение от 0 до 100", verbose_name='Скидка в процентах')
    product_in_discount = models.ManyToManyField(Products, help_text="Продукты, входящие в акцию",
                                                 verbose_name='Продукты, входящие в акцию')
    valid_from = models.DateTimeField(verbose_name='Время начала акции')
    valid_to = models.DateTimeField(verbose_name='Время конца акции')
    name.short_description = 'Название акции'

    def __str__(self):
        return self.name

    def count_product_id_discount(self):
        """Количество товаров, участвующих в акции"""
        count_product = list(Discount.objects.get(pk=self.pk).product_in_discount.all())
        return len(count_product)

    def get_product_in_discount(self):
        list_product_id_discount = list(Discount.objects.get(pk=self.pk).product_in_discount.all())
        return list_product_id_discount

    def get_sale(self):
        """Посчитать стоимость со скидкой и без скидки"""
        list_product_id_discount = Discount.objects.get(pk=self.pk).product_in_discount.all()
        price_without_discount = 0
        for i in list_product_id_discount:
            price_without_discount += i.price
        price_with_discount = price_without_discount * (100 - self.discount) / 100
        return f"Цена без скидки: {str(price_without_discount)},\n Цена со скидкой: {str(price_with_discount)}"

    # Переопределяем название столбцов в Админ-панели
    __str__.short_description = 'Название акции'
    count_product_id_discount.short_description = 'Количество продуктов в акции'
    get_product_in_discount.short_description = 'Список продуктов акции'
    get_sale.short_description = 'Сумма со скидкой'

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"
