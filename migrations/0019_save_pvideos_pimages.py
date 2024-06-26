# Generated by Django 4.1.6 on 2023-03-11 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stockex', '0018_transaction_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='save',
            fields=[
                ('saveid', models.AutoField(primary_key=True, serialize=False)),
                ('productid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stockex.product')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stockex.user')),
            ],
        ),
        migrations.CreateModel(
            name='pvideos',
            fields=[
                ('productVideoId', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=200)),
                ('productid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stockex.product')),
            ],
        ),
        migrations.CreateModel(
            name='pimages',
            fields=[
                ('productImageId', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=200)),
                ('productid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stockex.product')),
            ],
        ),
    ]
