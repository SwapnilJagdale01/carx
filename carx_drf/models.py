# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

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
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100)
    profilepic = models.ImageField(upload_to='static/profile/', blank=True, null=True) #models.CharField(db_column='profilePic', max_length=100)  # Field name made lowercase.
    socialid = models.CharField(db_column='socialId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    otp = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(blank=True, default=False)
    createdAt = models.DateTimeField(db_column='createdAt', null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class Makesmodel(models.Model):
    name = models.CharField(max_length=100)
    make = models.ForeignKey('Maker', models.DO_NOTHING, db_column='make')

    class Meta:
        managed = False
        db_table = 'MakesModel'

    def __str__(self):
        return self.name


class Maker(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'maker'

    def __str__(self):
        return self.name


class Vehicle(models.Model):

    make = models.ForeignKey(Maker, models.DO_NOTHING, db_column='make')
    model = models.ForeignKey(Makesmodel, models.DO_NOTHING, db_column='model')
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
        managed = False
        db_table = 'vehicle'