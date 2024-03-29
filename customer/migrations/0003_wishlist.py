# Generated by Django 5.0.2 on 2024-03-16 05:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_cart'),
        ('seller', '0004_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('products', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.product')),
            ],
        ),
    ]
