# Generated by Django 2.2.6 on 2019-10-26 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historialm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialm',
            name='fecha_inicio',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]