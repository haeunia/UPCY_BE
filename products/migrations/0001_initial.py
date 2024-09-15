# Generated by Django 4.0 on 2023-12-18 15:31

import django.db.models.deletion
from django.db import migrations, models

import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_alter_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('basic_price', models.CharField(max_length=500)),
                ('option', models.TextField(blank=True)),
                ('info', models.TextField(blank=True)),
                ('notice', models.TextField(blank=True)),
                ('period', models.CharField(blank=True, max_length=100)),
                ('transaction_direct', models.BooleanField(default=False)),
                ('transaction_package', models.BooleanField(default=False)),
                ('refund', models.TextField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category')),
                ('reformer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='product_photo.png', upload_to=products.models.get_product_photo_upload_path)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_photos', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductKeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keywords', to='products.product')),
            ],
        ),
    ]
