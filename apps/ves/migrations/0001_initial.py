# Generated by Django 3.0 on 2020-03-10 10:08

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descriptions', models.TextField(blank=True, max_length=500, verbose_name='описание')),
                ('name', models.CharField(blank=True, max_length=60, verbose_name='имя')),
                ('secondName', models.CharField(blank=True, max_length=60, verbose_name='отчество')),
                ('lastName', models.CharField(blank=True, max_length=60, verbose_name='фамилия')),
                ('role', models.CharField(blank=True, max_length=100, null=True, verbose_name='должность')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='дата рождения')),
                ('phone', models.CharField(max_length=30, null=True, verbose_name='телефон')),
                ('user_role', models.CharField(choices=[('guest', 'Гость'), ('operator', 'Оператор'), ('admin', 'Администратор'), ('kladovschik', 'Кладовщик')], default='guest', max_length=20, verbose_name='Роль пользователя')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Наименование')),
                ('description', models.TextField(default=None, verbose_name='Описание')),
                ('address', models.TextField(db_index=True, default=None, verbose_name='Адрес')),
                ('date_add', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('unp', models.BigIntegerField(verbose_name='УНП')),
            ],
            options={
                'verbose_name': 'Агент',
                'verbose_name_plural': 'Агенты',
            },
        ),
        migrations.CreateModel(
            name='Vagon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(db_index=True, max_length=255, verbose_name='Номер')),
                ('nakladnaya', models.CharField(db_index=True, default=0, max_length=255, verbose_name='Накладная')),
                ('date_add', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('last_in', models.DateTimeField(db_index=True, null=True, verbose_name='время последнего въезда')),
                ('last_out', models.DateTimeField(db_index=True, null=True, verbose_name='время последнего выезда')),
                ('ves_in', models.FloatField(db_index=True, null=True, verbose_name='вес на въезде')),
                ('ves_out', models.FloatField(db_index=True, null=True, verbose_name='вес на выезде')),
                ('netto', models.FloatField(db_index=True, null=True, verbose_name='полсденее нетто')),
                ('status_in', models.BooleanField(default=False, verbose_name='На территории?')),
                ('agent', models.ManyToManyField(to='ves.Agent')),
            ],
            options={
                'verbose_name': 'Вагон',
                'verbose_name_plural': 'Вагоны',
            },
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(db_index=True, max_length=255, verbose_name='Номер')),
                ('number_pricep', models.CharField(db_index=True, max_length=255, verbose_name='номер прицепа')),
                ('date_add', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('last_in', models.DateTimeField(db_index=True, null=True, verbose_name='время последнего въезда')),
                ('last_out', models.DateTimeField(db_index=True, null=True, verbose_name='время последнего выезда')),
                ('ves_in', models.FloatField(null=True, verbose_name='вес на въезде')),
                ('ves_out', models.FloatField(null=True, verbose_name='вес на выезде')),
                ('nakladnaya', models.CharField(db_index=True, default=0, max_length=255, verbose_name='Накладная')),
                ('netto', models.FloatField(null=True, verbose_name='полсденее нетто')),
                ('status_in', models.BooleanField(default=False, verbose_name='На территории?')),
                ('agent', models.ManyToManyField(to='ves.Agent')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='ActionUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('action', models.CharField(db_index=True, max_length=255, verbose_name='действие')),
                ('where', models.CharField(db_index=True, max_length=255, verbose_name='где')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('parentId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Журнал',
                'verbose_name_plural': 'Журналы',
            },
        ),
    ]
