from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone = models.CharField(max_length=10, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Почта')
    password = models.CharField(max_length=100, verbose_name='Пароль')

    def __str__(self):
        return f'{self.last_name} {self.last_name}'

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
