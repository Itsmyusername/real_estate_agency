from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    new_building = models.BooleanField('Новостройка', null=True)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    like = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Кто лайкнул', null=True, blank=True, related_name='likes')

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Кто жаловался', max_length=200, related_name='complaints')
    flat = models.ForeignKey(Flat, on_delete=models.PROTECT, verbose_name='Квартира, на которую пожаловались', related_name='complaints')
    text = models.CharField('Текст жалобы', max_length=500)

    def __str__(self):
        return self.user


class Owner(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО владельца')
    phonenumber = models.CharField('Номер владельца', max_length=20)
    pure_phone = PhoneNumberField('Нормализованный номер владельца', blank=True, null=True, region='RU')
    flats = models.ForeignKey(Flat, on_delete=models.PROTECT, verbose_name='Квартира в собственности', related_name='owners')

    def __str__(self):
        return self.name
