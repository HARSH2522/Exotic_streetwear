# Generated by Django 4.1.6 on 2023-03-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stockex', '0022_remove_product_adddate_product_pimg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='adddate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
