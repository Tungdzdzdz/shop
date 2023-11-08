# Generated by Django 4.2.5 on 2023-10-05 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_remove_product_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.size'),
        ),
        migrations.DeleteModel(
            name='ProductSize',
        ),
    ]