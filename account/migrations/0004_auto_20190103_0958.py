# Generated by Django 2.1.4 on 2019-01-03 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='token',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
