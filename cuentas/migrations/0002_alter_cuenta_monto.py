# Generated by Django 5.0 on 2023-12-21 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='monto',
            field=models.FloatField(default=0.0),
        ),
    ]
