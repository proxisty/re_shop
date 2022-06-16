from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.discount import Discount


@admin.register(Discount)
class AdminDiscount(admin.ModelAdmin):
    list_display = ['__str__', 'get_sale', 'count_product_id_discount', 'get_product_in_discount']
    filter_horizontal = ('product_in_discount',)


@admin.register(Products)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Customer)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'email', 'phone']


@admin.register(Order)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'customer']
