# Generated by Django 4.1.6 on 2023-03-08 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stockex', '0005_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
    ]
