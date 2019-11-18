# Generated by Django 2.2.6 on 2019-10-26 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historialm', '0003_auto_20191026_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operacion', models.CharField(max_length=20)),
                ('fecha_entrada', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='historialm',
            name='date_income',
        ),
    ]
