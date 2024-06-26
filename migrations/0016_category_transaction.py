# Generated by Django 4.1.6 on 2023-03-11 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stockex', '0015_productbid'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('catid', models.AutoField(primary_key=True, serialize=False)),
                ('catname', models.TextField(max_length=50)),
                ('status', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('tranid', models.AutoField(primary_key=True, serialize=False)),
                ('tranDate', models.DateField(null=True)),
                ('tranTime', models.TimeField(null=True)),
                ('tranamount', models.TextField(max_length=20)),
                ('status', models.TextField(max_length=10)),
            ],
        ),
    ]
