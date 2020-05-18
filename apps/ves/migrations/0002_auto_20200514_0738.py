# Generated by Django 3.0 on 2020-05-14 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ves', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Auto', models.BooleanField(default=False, verbose_name='Авто занято')),
                ('Zd', models.BooleanField(default=False, verbose_name='ЖД занято')),
            ],
        ),
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
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ves.Agent'),
        ),
        migrations.AddField(
            model_name='auto',
            name='driver',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Водитель'),
        ),
        migrations.AddField(
            model_name='auto',
            name='tara',
            field=models.IntegerField(null=True, verbose_name='Порожний'),
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
            name='Production',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='название')),
                ('auto_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ves.Auto')),
            ],
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
                ('productionId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ves.Production')),
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
                ('type', models.IntegerField(db_index=True, null=True, verbose_name='тип накладной')),
                ('number', models.BigIntegerField(db_index=True, null=True, verbose_name='номер в накладной')),
                ('seria', models.CharField(db_index=True, max_length=255, null=True, verbose_name='серия накладной')),
                ('name', models.CharField(db_index=True, max_length=255, null=True, verbose_name='наимеонвание')),
                ('price_one', models.FloatField(db_index=True, null=True, verbose_name='цена за ед')),
                ('price_no_nds', models.FloatField(db_index=True, null=True, verbose_name='цена  без ндс')),
                ('price', models.FloatField(db_index=True, null=True, verbose_name='цена')),
                ('nds', models.FloatField(db_index=True, null=True, verbose_name='НДС')),
                ('ves_nakladnaya', models.FloatField(db_index=True, null=True, verbose_name='вес по накладной')),
                ('price_ed', models.CharField(max_length=100, null=True, verbose_name='валюта')),
                ('ves_ed', models.CharField(max_length=100, null=True, verbose_name='еденицы измерения')),
                ('razreshil', models.CharField(db_index=True, max_length=255, null=True, verbose_name='кто разрешил')),
                ('pogruzka', models.CharField(db_index=True, max_length=255, null=True, verbose_name='место погрузки')),
                ('prinyal', models.CharField(db_index=True, max_length=255, null=True, verbose_name='кто принял')),
                ('putlist', models.BigIntegerField(db_index=True, null=True, verbose_name='номер путевого листа')),
                ('name_drive', models.CharField(db_index=True, max_length=255, null=True, verbose_name='имя водителя')),
                ('osnovanie', models.CharField(db_index=True, max_length=255, null=True, verbose_name='основание')),
                ('date', models.DateField(null=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('parentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ves.Auto')),
                ('productionId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ves.Production')),
            ],
            options={
                'verbose_name': 'Данные по накладной',
                'verbose_name_plural': 'Данные по накладным',
            },
        ),
        migrations.CreateModel(
            name='CatalogTrailer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tara', models.FloatField(db_index=True, null=True, verbose_name='вес')),
                ('number', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Номер')),
                ('marka', models.CharField(db_index=True, max_length=255, verbose_name='Марка')),
                ('model', models.CharField(db_index=True, max_length=255, verbose_name='Модель')),
                ('date_add', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ves.Agent')),
            ],
            options={
                'verbose_name': 'Прицеп',
                'verbose_name_plural': 'Прицепы',
            },
        ),
        migrations.CreateModel(
            name='CatalogAuto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tara', models.FloatField(db_index=True, null=True, verbose_name='вес')),
                ('number', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Номер')),
                ('marka', models.CharField(db_index=True, max_length=255, verbose_name='Марка')),
                ('model', models.CharField(db_index=True, max_length=255, verbose_name='Модель')),
                ('date_add', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ves.Agent')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.AddField(
            model_name='auto',
            name='catalog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ves.CatalogAuto'),
        ),
        migrations.AddField(
            model_name='auto',
            name='catalogPricep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ves.CatalogTrailer'),
        ),
    ]