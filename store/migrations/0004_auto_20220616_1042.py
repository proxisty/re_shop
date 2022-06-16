import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20220614_2251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterModelOptions(
            name='discount',
            options={'verbose_name': 'Скидка', 'verbose_name_plural': 'Скидки'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-quantity',), 'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=100, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='discount',
            field=models.IntegerField(help_text='Значение от 0 до 100', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Скидка в процентах'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='name',
            field=models.CharField(help_text='Максимальное значение 40', max_length=40, verbose_name='Название акции'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='product_in_discount',
            field=models.ManyToManyField(help_text='Продукты, входящие в акцию', to='store.Products', verbose_name='Продукты, входящие в акцию'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='valid_from',
            field=models.DateTimeField(verbose_name='Время начала акции'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='valid_to',
            field=models.DateTimeField(verbose_name='Время конца акции'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Адрес доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer', verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Дата заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Телефон заказчика'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.products', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Количество продукта'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Статус заказы'),
        ),
    ]
