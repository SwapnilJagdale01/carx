# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
FUEL_TYPE = (
    ('Petrol', 'Petrol'),
    ('Diesel', 'Diesel'),
    ('CNG', 'CNG'),
    ('LPG', 'LPG'),
)

TRANSMITION = (
    ('Automatic', 'Automatic'),
    ('Manual', 'Manual'),

)


class Customer(models.Model):
    mobile = models.CharField(max_length=30)
    profilepic = models.ImageField(upload_to='static/profile/', max_length=100, blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    socialId = models.CharField(max_length=500, blank=True, null=True, db_column='socialId')
    status = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'customer'


class Makermodel(models.Model):
    name = models.CharField(max_length=100)
    make = models.ForeignKey('Maker', models.DO_NOTHING, db_column='make')

    class Meta:
        managed = True
        db_table = 'makerModel'
        app_label = 'carx_drf'

    def __str__(self):
        return self.name


class Maker(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'maker'
        app_label = 'carx_drf'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'category'
        app_label = 'carx_drf'

    def __str__(self):
        return self.name


class Vehicle(models.Model):

    make = models.ForeignKey(Maker, models.DO_NOTHING, db_column='make')
    model = models.ForeignKey(Makermodel, models.DO_NOTHING, db_column='model')
    segment = models.CharField(max_length=200)
    verient = models.CharField(max_length=200)
    fuletype = models.CharField(db_column='fuleType', choices=FUEL_TYPE, max_length=100)  # Field name made lowercase.
    engine = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    capacity = models.CharField(max_length=100)
    output = models.CharField(max_length=100)
    torque = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100, choices=TRANSMITION)
    weight = models.CharField(max_length=100, blank=True, null=True)
    suspensiontype = models.CharField(db_column='suspensionType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    suspensionfront = models.CharField(db_column='suspensionFront', max_length=200, blank=True, null=True)  # Field name made lowercase.
    suspensionrear = models.CharField(db_column='suspensionRear', max_length=200, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    warranty = models.CharField(max_length=200, blank=True, null=True)
    onroadprice = models.CharField(db_column='onRoadPrice', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxclass = models.CharField(db_column='taxClass', max_length=100, blank=True, null=True)  # Field name made lowercase.
    image = models.ImageField(upload_to='static/vehicle/', blank=True, null=True)
    serviceschedule = models.CharField(db_column='serviceSchedule', max_length=200, blank=True, null=True)  # Field name made lowercase.
    seating = models.CharField(max_length=100, blank=True, null=True)
    fueltank = models.CharField(db_column='fuelTank', max_length=100, blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'vehicle'
        app_label = 'carx_drf'


class Tyre(models.Model):
    make = models.ForeignKey(Maker, models.DO_NOTHING, db_column='make')
    model = models.ForeignKey(Makermodel, models.DO_NOTHING, db_column='model')
    type = models.CharField(max_length=100)
    normalsectionwidth = models.CharField(db_column='normalSectionWidth', max_length=100, blank=True, null=True)  # Field name made lowercase.
    normalaspectratio = models.CharField(db_column='normalAspectRatio', max_length=100, blank=True, null=True)  # Field name made lowercase.
    constructiontype = models.CharField(db_column='constructionType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rimdiamter = models.CharField(db_column='rimDiamter', max_length=100, blank=True, null=True)  # Field name made lowercase.
    leadindex = models.CharField(db_column='leadIndex', max_length=100, blank=True, null=True)  # Field name made lowercase.
    speedsymbol = models.CharField(db_column='speedSymbol', max_length=100, blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category')
    pattern = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    warranty = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(max_length=200, blank=True, null=True, upload_to='static/tyres/')
    mrp = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tyre'
        app_label='carx_drf'

    def __str__(self):
        return self.type

