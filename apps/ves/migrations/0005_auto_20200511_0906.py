# Generated by Django 3.0 on 2020-05-11 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ves', '0004_auto_20200508_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='datanakladnayaauto',
            name='nds',
            field=models.FloatField(db_index=True, null=True, verbose_name='НДС'),
        ),
        migrations.AddField(
            model_name='datanakladnayaauto',
            name='price_no_nds',
            field=models.FloatField(db_index=True, null=True, verbose_name='цена  без ндс'),
        ),
        migrations.AddField(
            model_name='datanakladnayaauto',
            name='price_one',
            field=models.FloatField(db_index=True, null=True, verbose_name='цена за ед'),
        ),
        migrations.AddField(
            model_name='datanakladnayaauto',
            name='seria',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='серия накладной'),
        ),
        migrations.AddField(
            model_name='datanakladnayaauto',
            name='type',
            field=models.IntegerField(db_index=True, null=True, verbose_name='тип накладной'),
        ),
        migrations.AlterField(
            model_name='datanakladnayaauto',
            name='name',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='наимеонвание'),
        ),
        migrations.AlterField(
            model_name='datanakladnayaauto',
            name='number',
            field=models.BigIntegerField(db_index=True, null=True, verbose_name='номер в накладной'),
        ),
        migrations.AlterField(
            model_name='datanakladnayaauto',
            name='price',
            field=models.FloatField(db_index=True, null=True, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='datanakladnayaauto',
            name='price_ed',
            field=models.CharField(max_length=100, null=True, verbose_name='валюта'),
        ),
        migrations.AlterField(
            model_name='datanakladnayaauto',
            name='ves_ed',
            field=models.CharField(max_length=100, null=True, verbose_name='еденицы измерения'),
        ),
        migrations.AlterField(
            model_name='datanakladnayaauto',
            name='ves_nakladnaya',
            field=models.FloatField(db_index=True, null=True, verbose_name='вес по накладной'),
        ),
    ]
