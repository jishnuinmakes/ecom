# Generated by Django 4.1 on 2023-12-11 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_stock'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartTtem',
            new_name='CartItem',
        ),
    ]
