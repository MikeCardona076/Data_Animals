# Generated by Django 2.2.6 on 2019-10-26 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20191026_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='apellidos',
            field=models.CharField(default='SOME STRING', max_length=20),
        ),
    ]