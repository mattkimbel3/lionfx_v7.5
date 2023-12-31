# Generated by Django 3.2.16 on 2023-11-03 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0066_delete_cryptotrade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.CharField(max_length=10)),
                ('verification_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='account_id',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='account',
            name='currency',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='leverage',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
