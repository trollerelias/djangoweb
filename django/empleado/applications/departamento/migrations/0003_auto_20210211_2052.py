# Generated by Django 3.1.6 on 2021-02-12 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_auto_20210211_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='short_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Nombre corto'),
        ),
    ]