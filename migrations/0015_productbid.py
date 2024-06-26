# Generated by Django 4.1.6 on 2023-03-11 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stockex', '0014_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='productbid',
            fields=[
                ('prodbidid', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.TextField(max_length=20)),
                ('bidDateTime', models.DateTimeField(auto_now=True)),
                ('status', models.TextField(max_length=10)),
                ('productid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stockex.product')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stockex.user')),
            ],
        ),
    ]
