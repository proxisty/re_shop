import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Максимальное значение 40', max_length=40)),
                ('discount', models.IntegerField(help_text='Значение от 0 до 100',
                                                 validators=[django.core.validators.MinValueValidator(0),
                                                             django.core.validators.MaxValueValidator(100)])),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PromotionProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.discount')),
                ('discount_item', models.ManyToManyField(to='store.Products')),
            ],
        ),
    ]
