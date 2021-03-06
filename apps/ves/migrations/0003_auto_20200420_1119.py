# Generated by Django 3.0 on 2020-04-20 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ves', '0002_globaldata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto',
            name='agent',
        ),
        migrations.RemoveField(
            model_name='vagon',
            name='agent',
        ),
        migrations.AddField(
            model_name='auto',
            name='agents',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ves.Agent'),
        ),
        migrations.AddField(
            model_name='vagon',
            name='agent_vagon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ves.Agent'),
        ),
        migrations.AlterField(
            model_name='actionuser',
            name='parentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='agent',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Наименование'),
        ),
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
        migrations.CreateModel(
            name='DataNakladnayaAuto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.BigIntegerField(null=True, verbose_name='номер в накладной')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='действие')),
                ('price', models.FloatField(db_index=True, verbose_name='цена')),
                ('ves_nakladnaya', models.BigIntegerField(verbose_name='вес по накладной')),
                ('price_ed', models.CharField(max_length=100, verbose_name='валюта')),
                ('ves_ed', models.CharField(max_length=100, verbose_name='еденицы измерения')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('parentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ves.Auto')),
            ],
            options={
                'verbose_name': 'Данные по накладной',
                'verbose_name_plural': 'Данные по накладным',
            },
        ),
    ]
