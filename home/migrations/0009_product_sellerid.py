# Generated by Django 4.2.5 on 2023-09-24 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sellerId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.account'),
        ),
    ]
