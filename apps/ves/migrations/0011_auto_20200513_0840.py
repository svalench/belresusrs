# Generated by Django 3.0 on 2020-05-13 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ves', '0010_auto_tara'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogauto',
            name='number',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='catalogtrailer',
            name='number',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Номер'),
        ),
    ]
