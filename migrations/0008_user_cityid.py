# Generated by Django 4.1.6 on 2023-03-08 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stockex', '0007_user_contactno'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cityid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stockex.city'),
        ),
    ]