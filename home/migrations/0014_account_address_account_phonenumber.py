# Generated by Django 4.2.5 on 2023-09-27 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='phoneNumber',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
