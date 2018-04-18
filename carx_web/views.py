# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, render_to_response
from carx_web.forms import VehicleForm
from . forms import loginForm
from django.contrib.auth import logout,login
# Create your views here.
from django.contrib import messages
from carx_drf.models import Vehicle, Makermodel, Maker, Customer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponse
import json
from django.forms.models import model_to_dict


def dashboard(request):
    return render(request, 'carx_web/dashboard.html')


def login(request):
    form_data = request.POST
    # if request.POST:
    #     form = loginForm(request.POST or None)
    #     request.session['form_data'] = form_data
    # else:
    #     form = loginForm(request.session.get('form_data'))
    #
    # if form.is_valid():
    #     customer = Customer.objects.filter(email = form_data.get('username'), password= form_data.get('password'))
    #
    #     if customer:
    #         login(request, customer)
    #         return redirect('/home/')
    #     else:
    #         messages.success(request, "Enter Valid User Name and Password.")
    #         return redirect('/carx/login/')
    form = loginForm()
    return render(request, 'carx_login.html', {'form': form})


def logout(request):
    logout(request)
    return redirect('/carx/login/')


def create_vehicle(request):
    form = VehicleForm()
    return render(request,  'carx_web/createVehicle.html', {'form': form})


def save_vehicle(request):
    if request.POST:
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            # if(Vehicle.objects.filter(name=form.cleaned_data['name']).exists()):
            #     messages.warning(request, 'Record already exists with same name')
            # else:

            form.save()
            messages.success(request, 'Record added successfully')
            return redirect('/create/vehicle/')
        else:
            print form.errors
            return render(request, 'carx_web/createVehicle.html', {'form': form})
    else:
        form = VehicleForm()
        return render(request, 'carx_web/createVehicle.html', {'form': form})


def update_vehicle(request, pk):

        vehicle = Vehicle.objects.filter(id= pk)
        if vehicle:
            # if(Vehicle.objects.filter(name=form.cleaned_data['name']).exists()):
            #     messages.warning(request, 'Record already exists with same name')
            # else:
            form = VehicleForm(instance=vehicle[0])
            return render(request, 'carx_web/updateVehicle.html', {'form': form, 'id': vehicle[0].id, 'action':'view'})
        else:
            form= VehicleForm()
            messages.success(request, 'No record found')
            return render(request, 'carx_web/updateVehicle.html', {'form': form})


def update_vehicle_save(request, pk):

    vehicle = Vehicle.objects.filter(id=pk)
    if request.POST:
        form = VehicleForm(request.POST, instance=vehicle[0])
        if form.is_valid():
            # if(Vehicle.objects.filter(name=form.cleaned_data['name']).exists()):
            #     messages.warning(request, 'Record already exists with same name')
            # else:
            print "form valid"
            form.save()
            messages.success(request, 'Record Update successfully')
            return redirect('/vehicle/list')
        else:
            print form.errors
            return render(request, 'carx_web/updateVehicle.html', {'form': form})
    else:
        form = VehicleForm()
        return render(request, 'carx_web/updateVehicle.html', {'form': form})


def vehicle_list(request):

    vehicles_list = Vehicle.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(vehicles_list, 5)
    try:
        vehicles = paginator.page(page)
    except PageNotAnInteger:
        vehicles = paginator.page(1)
    except EmptyPage:
        vehicles = paginator.page(paginator.num_pages)

    return render(request, 'carx_web/vehicle_list.html', {'vehicles': vehicles})


def delete_vehicle(request, pk):

    vehicle = Vehicle.objects.filter(id=pk)

    try:
        if vehicle:
            vehicle.delete()
            messages.success(request, 'Record Delete successfully')
            return redirect('/vehicle/list')
    except:
        messages.warning(request, 'Record Delete successfully')
        return redirect('/vehicle/list')


def model_list(request):

    maker_id = request.GET.get('maker', None)

    models = Makermodel.objects.filter(make=maker_id)
    print maker_id
    data = []
    modelDict = []
    if models:
        for row in models:
            data.append(row)
            print data
        for secn in data:
            modelDict.append(model_to_dict(secn))
        return HttpResponse(json.dumps(modelDict), content_type="application/json")
    else:
        return HttpResponse(json.dumps(modelDict), content_type="application/json")
