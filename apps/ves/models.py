from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from ves_n import settings
from ves_n.setting_data import USER_ROLES_FOR_REDIRECTS_CHOICES


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    descriptions = models.TextField('описание', max_length=500, blank=True)
    name = models.CharField("имя", max_length=60, blank=True)
    secondName = models.CharField("отчество", max_length=60, blank=True)
    lastName = models.CharField("фамилия", max_length=60, blank=True)
    role = models.CharField("должность", max_length=100, null=True, blank=True)
    birth_date = models.DateField("дата рождения", null=True, blank=True)
    phone = models.CharField("телефон", max_length=30, null=True)
    user_role = models.CharField(max_length=20, choices=USER_ROLES_FOR_REDIRECTS_CHOICES,
                                 verbose_name='Роль пользователя', default=USER_ROLES_FOR_REDIRECTS_CHOICES[0][0])




class Agent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Наименование', max_length=255, unique=True, db_index=True)
    description = models.TextField('Описание', default=None)
    address = models.TextField('Адрес', default=None, db_index=True)
    date_add = models.DateTimeField(auto_now_add=True, db_index=True)
    date_update = models.DateTimeField(auto_now=True)
    unp = models.BigIntegerField('УНП')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Агент'
        verbose_name_plural = 'Агенты'



class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    agents = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True)
    number = models.CharField('Номер', max_length=255, db_index=True)
    number_pricep =  models.CharField('номер прицепа', max_length=255, db_index=True)
    date_add = models.DateTimeField(auto_now_add=True, db_index=True)
    date_update = models.DateTimeField(auto_now=True)
    last_in = models.DateTimeField('время последнего въезда', null=True, db_index=True)
    last_out = models.DateTimeField('время последнего выезда',  null=True, db_index=True)
    ves_in = models.FloatField('вес на въезде',  null=True)
    ves_out = models.FloatField('вес на выезде', null=True)
    nakladnaya = models.CharField('Накладная', max_length=255, default=0, db_index=True)
    netto = models.FloatField("полсденее нетто",  null=True)
    status_in = models.BooleanField('На территории?', default= False)
    def __str__(self):
        return self.number
    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Vagon(models.Model):
    id = models.AutoField(primary_key=True)
    agent_vagon = models.ForeignKey('Agent', on_delete=models.CASCADE, null=True, blank=True)
    number = models.CharField('Номер', max_length=255, db_index=True)
    nakladnaya = models.CharField('Накладная', max_length=255, default=0, db_index=True)
    date_add = models.DateTimeField(auto_now_add=True, db_index=True)
    date_update = models.DateTimeField(auto_now=True)
    last_in = models.DateTimeField('время последнего въезда',  null=True, db_index=True)
    last_out = models.DateTimeField('время последнего выезда', null=True, db_index=True)
    ves_in = models.FloatField('вес на въезде',  null=True, db_index=True)
    ves_out = models.FloatField('вес на выезде',  null=True, db_index=True)
    netto = models.FloatField("полсденее нетто", null=True, db_index=True)
    status_in = models.BooleanField('На территории?', default= False)
    def __str__(self):
        return self.number
    class Meta:
        verbose_name = 'Вагон'
        verbose_name_plural = 'Вагоны'

class ActionUser(models.Model):
    id = models.AutoField(primary_key=True)
    parentId = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField('действие', max_length=255, db_index=True)
    where = models.CharField('где', max_length=255, db_index=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'

class DataNakladnayaAuto(models.Model):
    id = models.AutoField(primary_key=True)
    parentId = models.ForeignKey(Auto, on_delete=models.CASCADE)
    number = models.BigIntegerField('номер в накладной', null=True)
    name = models.CharField('действие', max_length=255, db_index=True)
    price = models.FloatField('цена', db_index=True)
    ves_nakladnaya = models.BigIntegerField('вес по накладной')
    price_ed = models.CharField('валюта', max_length=100)
    ves_ed = models.CharField('еденицы измерения', max_length=100)
    date_add = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Данные по накладной'
        verbose_name_plural = 'Данные по накладным'

class DataNakladnayaVagon(models.Model):
    id = models.AutoField(primary_key=True)
    parentId = models.ForeignKey(Vagon, on_delete=models.CASCADE)
    number = models.BigIntegerField('номер в накладной', null=True)
    name = models.CharField('действие', max_length=255, db_index=True)
    price = models.FloatField('цена', db_index=True)
    ves_nakladnaya = models.BigIntegerField('вес по накладной')
    price_ed = models.CharField('валюта', max_length=100)
    ves_ed = models.CharField('еденицы измерения', max_length=100)
    date_add = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Данные по накладной'
        verbose_name_plural = 'Данные по накладным'