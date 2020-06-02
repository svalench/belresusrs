from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from ves_n import settings
from ves_n.setting_data import USER_ROLES_FOR_REDIRECTS_CHOICES

class GlobalData(models.Model):
    id = models.AutoField(primary_key=True)
    Auto = models.BooleanField('Авто занято',default=False)
    Zd   = models.BooleanField("ЖД занято", default=False)


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
    def is_admin(self):
        if(self.user_role==USER_ROLES_FOR_REDIRECTS_CHOICES[2][0]):
            return True
        else:
            return False


class CatalogResponsiblePerson(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField("имя", max_length=100, null=True, blank=True)
    second_name = models.CharField("отчество", max_length=100, null=True, blank=True)
    last_name = models.CharField("фамилия", max_length=100, null=True, blank=True)
    role = models.CharField("должность", max_length=100, null=True, blank=True)


class Production(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('название', max_length=255, db_index=True)
    number = models.CharField('номер',null=True ,max_length=255, db_index=True)
    characteristicTMC = models.CharField('характеристика ТМЦ', null=True, max_length=255, db_index=True)
    typeTMC = models.CharField('тип ТМЦ', max_length=255, null=True, db_index=True)
    scoreTMC = models.CharField('счет ТМЦ', max_length=255, null=True, db_index=True)
    score = models.CharField('счет', max_length=255, null=True, db_index=True)
    typeOfAccountTMC = models.CharField('вид учета ТМЦ', null=True, max_length=255, db_index=True)


class Agent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Наименование', max_length=255, unique=True, db_index=True)
    description = models.TextField('Описание', default=None)
    address = models.TextField('Адрес', default=None, db_index=True)
    date_add = models.DateTimeField(auto_now_add=True, db_index=True)
    date_update = models.DateTimeField(auto_now=True)
    unp = models.BigIntegerField('УНП')
    dischargePoint = models.TextField('пункт разгрузки', db_index=True, null=True)
    payer = models.TextField('плательщик', db_index=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Агент'
        verbose_name_plural = 'Агенты'



class CatalogContract(models.Model):
    id = models.AutoField(primary_key=True)
    parentMaterialId = models.ForeignKey('Production', on_delete=models.CASCADE, null=True, blank=True,
                                         db_index=True)
    parentContragentId = models.ForeignKey('Agent', on_delete=models.CASCADE, null=True, blank=True,
                                         db_index=True)
    name = models.CharField('название контракта',max_length=255, db_index=True)
    date =  models.DateField("дата", null=True, blank=True)
    typeOfOperation = models.CharField('тип опреации',max_length=255, db_index=True)
    typeOfArrival = models.CharField('вид прихода',max_length=255, db_index=True)
    salesAccount = models.CharField('счет реализации', max_length=255, db_index=True)





class CatalogTrailer(models.Model):
    id = models.AutoField(primary_key=True)
    tara = models.FloatField('вес', null=True, db_index=True)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE, null=True, blank=True, db_index=True)
    number = models.CharField('Номер',unique=True, max_length=255, db_index=True)
    marka = models.CharField('Марка', max_length=255, db_index=True)
    model = models.CharField('Модель', max_length=255, db_index=True)
    date_add = models.DateTimeField(auto_now_add=True, db_index=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Прицеп'
        verbose_name_plural = 'Прицепы'


class CatalogAuto(models.Model):
    id = models.AutoField(primary_key=True)
    tara = models.FloatField('вес', null=True, db_index=True)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE, null=True, blank=True, db_index=True)
    number = models.CharField('Номер',unique=True, max_length=255, db_index=True)
    marka = models.CharField('Марка', max_length=255, db_index=True)
    model = models.CharField('Модель', max_length=255, db_index=True)
    date_add = models.DateTimeField(auto_now_add=True, db_index=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    agents = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, blank=True,db_index=True)
    catalog = models.ForeignKey(CatalogAuto, on_delete=models.SET_NULL, null=True, blank=True, db_index=True)
    catalogPricep = models.ForeignKey(CatalogTrailer, on_delete=models.SET_NULL, null=True, blank=True, db_index=True)
    parentUserId = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True,
                                     db_index=True)
    parentResponseId = models.ForeignKey('CatalogResponsiblePerson', on_delete=models.CASCADE, null=True, blank=True,
                                         db_index=True)
    parentContractId = models.ForeignKey('CatalogContract', on_delete=models.CASCADE, null=True, blank=True,
                                         db_index=True)



    number = models.CharField('Номер', max_length=255, db_index=True)
    driver = models.CharField('Водитель', max_length=255,null=True ,db_index=True)
    number_pricep =  models.CharField('номер прицепа', max_length=255,null=True, db_index=True)
    date_add = models.DateTimeField(auto_now_add=True, db_index=True)
    date_update = models.DateTimeField(auto_now=True)
    last_in = models.DateTimeField('время последнего въезда', null=True, db_index=True)
    last_out = models.DateTimeField('время последнего выезда',  null=True, db_index=True)
    weghtIn = models.FloatField('вес пустой', null=True, db_index=True)
    weghtOut = models.FloatField('вес полной', null=True, db_index=True)
    netto = models.FloatField('вес clear', null=True, db_index=True)
    status_in = models.BooleanField('На территории?', default=False)
    description = models.TextField('описание',null=True, db_index=True)
    numberPassport = models.CharField('номер сопрводительного пасопрта', max_length=255, null=True, db_index=True)
    store = models.CharField('склад', max_length=255, null=True, db_index=True)
    discont = models.FloatField('скидка', null=True, db_index=True)
    organization = models.CharField('организация', max_length=255, null=True, db_index=True)
    courseDate = models.DateField("дата курса ", null=True, blank=True)
    nakladnayaDate = models.DateField("дата накладной ", null=True, blank=True)

    #typeOperation = models.CharField('тип операции', max_length=255, null=True, db_index=True)
    executer = models.CharField('исполнитель', max_length=255, null=True, db_index=True)
    numberAttorney = models.CharField('номер доверенности', max_length=255, null=True, db_index=True)
    numberSeats = models.CharField('количество мест', max_length=255, null=True, db_index=True)
    type = models.IntegerField('тип накладной', null=True, db_index=True)
    numberNakladnaia = models.BigIntegerField('номер в накладной', null=True, db_index=True)
    seria = models.CharField('серия накладной', max_length=255, null=True, db_index=True)
    price_no_nds = models.FloatField('цена  без ндс', null=True, db_index=True)
    price_ed_iz = models.FloatField('цена ed', null=True, db_index=True)
    price = models.FloatField('цена', null=True, db_index=True)
    nds = models.FloatField('НДС', null=True, db_index=True)
    ves_nakladnaya = models.FloatField('вес по накладной', null=True, db_index=True)
    price_ed = models.CharField('валюта', null=True, max_length=100)
    ves_ed = models.CharField('еденицы измерения', null=True, max_length=100)
    razreshil = models.CharField('кто разрешил', null=True, max_length=255, db_index=True)
    pogruzka = models.CharField('место погрузки', null=True, max_length=255, db_index=True)
    prinyal = models.CharField('кто принял', null=True, max_length=255, db_index=True)
    putlist = models.BigIntegerField('номер путевого листа', null=True, db_index=True)
    osnovanie = models.CharField('основание', max_length=255, null=True, db_index=True)
    def __str__(self):
        return self.number
    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'




class Vagon(models.Model):
    id = models.AutoField(primary_key=True)
    agent_vagon = models.ForeignKey('Agent', on_delete=models.CASCADE, null=True, blank=True, db_index=True)
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
    parentId = models.ForeignKey('Auto', on_delete=models.CASCADE)
    productionId = models.ForeignKey('Production', null=True, on_delete=models.CASCADE)
    type = models.IntegerField('тип накладной', null=True,db_index=True)
    number = models.BigIntegerField('номер в накладной', null=True,db_index=True)
    seria = models.CharField('серия накладной',max_length=255,null=True,db_index=True)
    name = models.CharField('наимеонвание',  null=True,max_length=255, db_index=True)
    price_one = models.FloatField('цена за ед', null=True, db_index=True)
    price_no_nds = models.FloatField('цена  без ндс', null=True, db_index=True)
    price = models.FloatField('цена',  null=True, db_index=True)
    nds = models.FloatField('НДС',null=True,db_index=True)
    ves_nakladnaya = models.FloatField('вес по накладной',  null=True,db_index=True)
    price_ed = models.CharField('валюта',  null=True, max_length=100)
    ves_ed = models.CharField('еденицы измерения',  null=True, max_length=100)
    razreshil = models.CharField('кто разрешил',null=True,max_length=255,db_index=True)
    pogruzka = models.CharField('место погрузки',null=True,max_length=255,db_index=True)
    prinyal = models.CharField('кто принял', null=True, max_length=255, db_index=True)
    putlist = models.BigIntegerField('номер путевого листа', null=True, db_index=True)
    name_drive =  models.CharField('имя водителя',max_length=255,  null=True, db_index=True)
    osnovanie = models.CharField('основание',max_length=255,  null=True, db_index=True)
    date = models.DateField(null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Данные по накладной'
        verbose_name_plural = 'Данные по накладным'

class DataNakladnayaVagon(models.Model):
    id = models.AutoField(primary_key=True)
    parentId = models.ForeignKey('Vagon', on_delete=models.CASCADE)
    productionId = models.ForeignKey(Production,null=True, on_delete=models.CASCADE)
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


