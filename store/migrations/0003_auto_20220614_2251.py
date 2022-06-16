from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('store', '0002_discount_promotionproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='product_in_discount',
            field=models.ManyToManyField(to='store.Products'),
        ),
        migrations.DeleteModel(
            name='PromotionProducts',
        ),
    ]
