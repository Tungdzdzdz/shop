# Generated by Django 4.2.5 on 2023-11-03 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_product_sell'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='show',
            field=models.IntegerField(default=0),
        ),
    ]
