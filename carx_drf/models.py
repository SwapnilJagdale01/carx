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

VEHICLE_TYPE = (
    ('2 Wheeler', '2 Wheeler'),
    ('4 Wheeler', '4 Wheeler'),
    ('Commercial', 'Commercial'),
)


class Customer(models.Model):
    mobile = models.CharField(max_length=30, unique=True)
    profilepic = models.ImageField(upload_to='static/profile/', max_length=100, blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200, unique=True)
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

    vehicle_type = models.CharField(db_column='vehicleType', choices=VEHICLE_TYPE, blank=False, max_length=100)
    make = models.ForeignKey(Maker, models.DO_NOTHING, db_column='make')
    model = models.ForeignKey(Makermodel, models.DO_NOTHING, db_column='model')
    name = models.CharField(max_length=100)
    segment = models.CharField(max_length=200)
    verient = models.CharField(max_length=200)
    fuletype = models.CharField(db_column='fuleType', choices=FUEL_TYPE, max_length=100)  # Field name made lowercase.
    engine = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    capacity = models.CharField(max_length=100)
    output = models.CharField(max_length=100)
    torque = models.CharField(max_length=100)
    transmission_type = models.CharField(max_length=100, choices=TRANSMITION)
    transmission = models.CharField(max_length=100, blank=True, null=True)
    weight = models.CharField(max_length=100, blank=True, null=True)
    suspensiontype = models.CharField(db_column='suspensionType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    length = models.CharField(max_length=200, blank=True, null=True)  # Field name made lowercase.
    width = models.CharField(max_length=200, blank=True, null=True)  # Field name made lowercase.
    height = models.CharField(max_length=200, blank=True, null=True)  # Field name made lowercase
    startdate = models.PositiveSmallIntegerField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.PositiveSmallIntegerField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    steering = models.CharField(max_length=100, blank=True, null=True)
    type_and_wheel = models.CharField(db_column='typeAndwheel', max_length=200, blank=True, null=True)
    breaks = models.CharField(db_column='breaks', max_length=100, blank=True, null=True)  # Field name made lowercase.
    image = models.ImageField(upload_to='static/vehicle/', blank=True, null=True)
    ground_clearance = models.CharField(db_column='groundClearance', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fueltank = models.CharField(db_column='fuelTank', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mileage = models.CharField(db_column='mileage', max_length=100, blank=False)
    scaling = models.CharField(db_column='scaling', max_length=100, blank=True)
    turning_radius = models.CharField(db_column='turningRadius', max_length=100, blank=True)

    class Meta:
        managed = True
        db_table = 'vehicle'
        app_label = 'carx_drf'

    def __str__(self):
        return self.name


class Tyre(models.Model):
    vehicle = models.ForeignKey(Vehicle,  null=True,blank=True,db_column='vahicle',on_delete=models.PROTECT)
    product_type = models.CharField(max_length=100)
    normalsectionwidth = models.CharField(db_column='normalSectionWidth', max_length=100, blank=True, null=True)  # Field name made lowercase.
    normalaspectratio = models.CharField(db_column='normalAspectRatio', max_length=100, blank=True, null=True)  # Field name made lowercase.
    constructiontype = models.CharField(db_column='constructionType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rimdiamter = models.CharField(db_column='rimDiamter', max_length=100, blank=True, null=True)  # Field name made lowercase.
    loadindex = models.CharField(db_column='leadIndex', max_length=100, blank=True, null=True)  # Field name made lowercase.
    speedsymbol = models.CharField(db_column='speedSymbol', max_length=100, blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey(Category,  db_column='category' ,null=True,blank=True,on_delete=models.PROTECT)
    pattern = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    warranty = models.CharField(max_length=100, blank=True, null=True)
    warranty_summery = models.CharField(max_length=500, blank=True, null=True)
    left_image = models.CharField(max_length=500, blank=True, null=True )
    right_image = models.CharField(max_length=500, blank=True, null=True )
    front_image = models.CharField(max_length=500, blank=True, null=True )
    back_image = models.CharField(max_length=500, blank=True, null=True)
    mrp = models.CharField(max_length=100, blank=True, null=True)
    construction_type_R=models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tyre'
        app_label='carx_drf'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

