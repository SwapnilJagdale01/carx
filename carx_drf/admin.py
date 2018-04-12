# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Vehicle, Maker, Makermodel, Category, Tyre
from django.contrib.contenttypes.admin import GenericTabularInline


admin.site.register(Makermodel)
admin.site.register(Maker)
admin.site.register(Vehicle)
admin.site.register(Category)
admin.site.register(Tyre)