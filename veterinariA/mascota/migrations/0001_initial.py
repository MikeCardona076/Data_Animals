# Generated by Django 2.2.6 on 2019-10-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('raza', models.TextField()),
                ('sexo', models.TextField()),
                ('edad', models.TextField()),
            ],
        ),
    ]
