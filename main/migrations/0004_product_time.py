# Generated by Django 5.1.1 on 2024-09-24 11:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_delete_buyentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='time',
            field=models.DateField(auto_now_add=True, default=datetime.date(2024, 9, 24)),
            preserve_default=False,
        ),
    ]