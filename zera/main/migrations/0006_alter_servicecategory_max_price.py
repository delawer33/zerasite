# Generated by Django 4.2.3 on 2023-08-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_servicecategory_max_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecategory',
            name='max_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Максимальная цена'),
        ),
    ]