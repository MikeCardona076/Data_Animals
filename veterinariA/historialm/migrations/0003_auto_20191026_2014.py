# Generated by Django 2.2.6 on 2019-10-26 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historialm', '0002_auto_20191026_2012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historialm',
            old_name='fecha_inicio',
            new_name='date_income',
        ),
    ]
