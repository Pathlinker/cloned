# Generated by Django 2.1b1 on 2018-07-08 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20180708_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='cat_id',
            new_name='item_cat_id',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='subcat_id',
            new_name='item_subcat_id',
        ),
        migrations.RenameField(
            model_name='subcat',
            old_name='parentid',
            new_name='subcategory_parentid',
        ),
        migrations.RenameField(
            model_name='subcat',
            old_name='subparentid',
            new_name='subcategory_subcatparentid',
        ),
    ]