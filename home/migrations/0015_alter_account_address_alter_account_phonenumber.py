# Generated by Django 4.2.5 on 2023-09-27 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_account_address_account_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='address',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]