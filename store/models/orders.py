from django.db import models
from .product import Products
from .customer import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Продукт')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Пользователь')
    quantity = models.IntegerField(default=1, verbose_name='Количество продукта')
    price = models.IntegerField(verbose_name='Цена')
    address = models.CharField(max_length=50, default='', blank=True, verbose_name='Адрес доставки')
    phone = models.CharField(max_length=50, default='', blank=True, verbose_name='Телефон заказчика')
    date = models.DateField(default=datetime.datetime.today, verbose_name='Дата заказа')
    status = models.BooleanField(default=False, verbose_name='Статус заказы')

    def __str__(self):
        return f"Заказ продукта '{self.product}' в количестве {self.quantity} на сумму {self.get_cost()}"

    def placeOrder(self):
        self.save()

    def get_cost(self):
        """ Получить стоимость заказа"""
        return self.price * self.quantity

    @staticmethod
    def get_orders_by_customer(customer_id=None):
        return Order.objects.filter(customer=customer_id).order_by('-date')

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ('-quantity',)
