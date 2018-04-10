# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Vehicle, Maker, Makesmodel
from django.contrib.contenttypes.admin import GenericTabularInline


admin.site.register(Makesmodel)
admin.site.register(Maker)
admin.site.register(Vehicle)