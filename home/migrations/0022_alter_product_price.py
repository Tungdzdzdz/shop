# Generated by Django 4.2.5 on 2023-09-30 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_remove_category_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]