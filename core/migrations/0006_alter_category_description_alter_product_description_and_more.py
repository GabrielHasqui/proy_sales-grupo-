# Generated by Django 4.2 on 2024-05-29 02:23

from decimal import Decimal
from django.db import migrations, models
import proy_sales.utils


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_product_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=100, validators=[proy_sales.utils.valida_letras], verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=100, validators=[proy_sales.utils.valida_letras], verbose_name='Articulo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=10, validators=[proy_sales.utils.valida_decimal], verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=100, help_text='Stock debe estar en 0 y 10000 unidades', validators=[proy_sales.utils.valida_numero], verbose_name='Stock'),
        ),
    ]
