# Generated by Django 3.2.16 on 2023-11-03 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0068_auto_20231103_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_id',
            field=models.PositiveSmallIntegerField(),
        ),
    ]