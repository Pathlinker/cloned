# Generated by Django 2.1b1 on 2018-07-08 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20180708_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_description',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_discount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_unit',
            field=models.CharField(default=False, max_length=16),
        ),
    ]
