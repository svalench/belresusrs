# Generated by Django 3.0 on 2020-03-17 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ves', '0006_auto_20200317_0644'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataNakladnayaVagon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.BigIntegerField(null=True, verbose_name='номер в накладной')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='действие')),
                ('price', models.FloatField(db_index=True, verbose_name='цена')),
                ('ves_nakladnaya', models.BigIntegerField(verbose_name='вес по накладной')),
                ('price_ed', models.CharField(max_length=100, verbose_name='валюта')),
                ('ves_ed', models.CharField(max_length=100, verbose_name='еденицы измерения')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('parentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ves.Vagon')),
            ],
            options={
                'verbose_name': 'Данные по накладной',
                'verbose_name_plural': 'Данные по накладным',
            },
        ),
    ]
