# Generated by Django 3.2.7 on 2021-09-08 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0005_auto_20210812_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutricalc',
            name='food_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diet.base', verbose_name='ALIMENTO'),
        ),
    ]
