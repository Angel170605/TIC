# Generated by Django 5.2.2 on 2025-06-08 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_cart_price_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('description', models.TextField()),
                ('input_text', models.CharField(blank=True, max_length=250, null=True)),
                ('input_image', models.ImageField(blank=True, default='profiles/default.png', null=True, upload_to='users_input_images')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_products', to='shop.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='on_carts', to='shop.product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(blank=True, related_name='products', through='shop.CartProduct', to='shop.product'),
        ),
    ]
