# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, render_to_response
from datetime import datetime
from carx_web.forms import VehicleForm,loginForm,category_form,maker_form,tyre_form
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages
from carx_drf.models import Vehicle, Makermodel, Maker, Customer,Category,Tyre
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponse
import json
from django.forms.models import model_to_dict
from django.conf import settings
from .resources import TyreResource
from django.http import HttpResponse
from tablib import Dataset
import xlwt
import os

@login_required(login_url='/')
def Home(request):
    return render(request, 'dashboard.html')


def Login(request):
    form_data = request.POST
    if request.POST:
        form = loginForm(request.POST or None)
        request.session['form_data'] = form_data
    else:
        form = loginForm(request.session.get('form_data'))

    if form.is_valid():
        user = form.login(request)

        if user:
            login(request, user)
            return redirect('home/')
        else:
            messages.success(request, "Enter Valid User Name and Password.")
            form = loginForm()
            return render(request, 'carx_login.html', {'form': form})

    return render(request,'carx_login.html', {'form':form})


def Logout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/')
def create_vehicle(request):
    form = VehicleForm()
    return render(request,  'createVehicle.html', {'form': form})

@login_required(login_url='/')
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
            return render(request, 'createVehicle.html', {'form': form})
    else:
        form = VehicleForm()
        return render(request, 'createVehicle.html', {'form': form})


@login_required(login_url='/')
def update_vehicle(request, pk):

        vehicle = Vehicle.objects.filter(id= pk)
        if vehicle:
            # if(Vehicle.objects.filter(name=form.cleaned_data['name']).exists()):
            #     messages.warning(request, 'Record already exists with same name')
            # else:
            form = VehicleForm(instance=vehicle[0])
            return render(request, 'updateVehicle.html', {'form': form, 'id': vehicle[0].id, 'action':'view'})
        else:
            form= VehicleForm()
            messages.success(request, 'No record found')
            return render(request, 'updateVehicle.html', {'form': form})


@login_required(login_url='/')
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
            return render(request, 'updateVehicle.html', {'form': form})
    else:
        form = VehicleForm()
        return render(request, 'updateVehicle.html', {'form': form})


@login_required(login_url='/')
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

    return render(request, 'vehicle_list.html', {'vehicles': vehicles})


@login_required(login_url='/')
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

@login_required(login_url='/')
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


@login_required(login_url='/')
def SaveTyre(request):
    if request.POST:
        form=tyre_form(request.POST, request.FILES)
        if form.is_valid():
            tyre = form.save()
            if form.cleaned_data['left_image']:
                dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
                filename = "%s_%s.%s" % (tyre.name+form.cleaned_data['left_image'].name, dirname, 'png')
                raw_file_path_and_name = os.path.join('tyres', filename)
                with open(settings.MEDIA_ROOT + raw_file_path_and_name, 'wb')as f:
                    for chunk in form.cleaned_data['left_image'].chunks():
                        f.write(chunk)
                tyre.left_image = raw_file_path_and_name

            if form.cleaned_data['right_image']:
                dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
                filename = "%s_%s.%s" % (tyre.name+form.cleaned_data['right_image'].name, dirname, 'png')
                raw_file_path_and_name = os.path.join('tyres', filename)
                with open(settings.MEDIA_ROOT + raw_file_path_and_name, 'wb')as f:
                    for chunk in form.cleaned_data['right_image'].chunks():
                        f.write(chunk)
                tyre.right_image = raw_file_path_and_name
            if form.cleaned_data['front_image']:
                dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
                filename = "%s_%s.%s" % (tyre.name+form.cleaned_data['front_image'].name, dirname, 'png')
                raw_file_path_and_name = os.path.join('tyres', filename)
                with open(settings.MEDIA_ROOT + raw_file_path_and_name, 'wb')as f:
                    for chunk in form.cleaned_data['front_image'].chunks():
                        f.write(chunk)
                tyre.front_image = raw_file_path_and_name
            if form.cleaned_data['back_image']:
                dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
                filename = "%s_%s.%s" % (tyre.name+form.cleaned_data['back_image'].name, dirname, 'png')
                raw_file_path_and_name = os.path.join('tyres', filename)
                with open(settings.MEDIA_ROOT + raw_file_path_and_name, 'wb')as f:
                    for chunk in form.cleaned_data['back_image'].chunks():
                        f.write(chunk)
                tyre.back_image = raw_file_path_and_name

            tyre.save()
            messages.success(request, 'Record added successfully')
        return redirect('/tyre_list/')
    else:
        form =tyre_form()
    return render(request, 'tyre_list.html',{'form':form} )


@login_required(login_url='/')
def SaveCategory(request):
    if request.POST:
        form=category_form(request.POST)
        if form.is_valid():
            if(Category.objects.filter(name=form.cleaned_data['name']).exists()):
                messages.warning(request, 'Category already exists with same name')
            else:
                form.save()
                messages.success(request, 'Category added successfully')
        return redirect('/category_list/')
    else:
        form =category_form()
    return render(request, 'category.html',{'form':form} )

@login_required(login_url='/')
def ViewCategory(request,category_id):
    category_rec = Category.objects.filter(id=category_id)
    if category_rec:
        form = category_form(instance=category_rec[0])
        return render(request, 'update_category.html', {'form': form,'id':category_rec[0].id,'action':'view'})

@login_required(login_url='/')
def ViewTyre(request,tyre_id):
    tyre_rec = Tyre.objects.filter(id=tyre_id)
    if tyre_rec:
        form = tyre_form(instance=tyre_rec[0])
        path = 'http://' + request.META['HTTP_HOST'] + '/media/'
        return render(request, 'update_tyre.html', {'form': form, 'id': tyre_rec[0].id, 'action': 'view',
                                                    'path':path,'tyre_rec':tyre_rec[0]})

@login_required(login_url='/')
def UpdateTyre(request,tyre_id):
    tyre_rec = Tyre.objects.filter(id=tyre_id)
    path = 'http://' + request.META['HTTP_HOST'] + '/media/'
    if request.POST:
        form = tyre_form(request.POST, request.FILES,instance=tyre_rec[0])
        if form.is_valid():
            tyre = form.save()
            if tyre.left_image != form.cleaned_data['left_image']:
                dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
                filename = "%s_%s.%s" % (tyre.name + form.cleaned_data['left_image'].name, dirname, 'png')
                raw_file_path_and_name = os.path.join('tyres', filename)
                with open(settings.MEDIA_ROOT + raw_file_path_and_name, 'wb')as f:
                    for chunk in form.cleaned_data['left_image'].chunks():
                        f.write(chunk)
                tyre.left_image = raw_file_path_and_name

            if tyre.right_image != form.cleaned_data['right_image']:
                dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
                filename = "%s_%s.%s" % (tyre.name + form.cleaned_data['right_image'].name, dirname, 'png')
                raw_file_path_and_name = os.path.join('tyres', filename)
                with open(settings.MEDIA_ROOT + raw_file_path_and_name, 'wb')as f:
                    for chunk in form.cleaned_data['right_image'].chunks():
                        f.write(chunk)
                tyre.right_image = raw_file_path_and_name
            if tyre.front_image != form.cleaned_data['front_image']:
                dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
                filename = "%s_%s.%s" % (tyre.name + form.cleaned_data['front_image'].name, dirname, 'png')
                raw_file_path_and_name = os.path.join('tyres', filename)
                with open(settings.MEDIA_ROOT + raw_file_path_and_name, 'wb')as f:
                    for chunk in form.cleaned_data['front_image'].chunks():
                        f.write(chunk)
                tyre.front_image = raw_file_path_and_name
            if tyre.back_image != form.cleaned_data['back_image']:
                dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
                filename = "%s_%s.%s" % (tyre.name + form.cleaned_data['back_image'].name, dirname, 'png')
                raw_file_path_and_name = os.path.join('tyres', filename)
                with open(settings.MEDIA_ROOT + raw_file_path_and_name, 'wb')as f:
                    for chunk in form.cleaned_data['back_image'].chunks():
                        f.write(chunk)
                tyre.back_image = raw_file_path_and_name
            tyre.save()
            messages.success(request, 'Tyre updated successfully')
        return redirect('/tyre_list/')
    else:

        form = tyre_form(instance=tyre_rec[0])
        return render(request, 'update_tyre.html', {'form': form, 'id': tyre_rec[0].id, 'action': 'update',
                                                    'path':path,'tyre_rec':tyre_rec[0]})

@login_required(login_url='/')
def UpdateCategory(request,category_id):
    category_rec = Category.objects.filter(id=category_id)
    if request.POST:
        form = category_form(request.POST,instance=category_rec[0])
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully')

        return redirect('/category_list/')
    else :
        form = category_form(instance=category_rec[0])
        return render(request, 'update_category.html', {'form': form,'id':category_rec[0].id,'action':'update'})

@login_required(login_url='/')
def CategoryList(request):

    category_list = Category.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(category_list, 10)
    try:
        cat_list = paginator.page(page)
    except PageNotAnInteger:
        cat_list = paginator.page(1)
    except EmptyPage:
        cat_list = paginator.page(paginator.num_pages)
    return render(request, 'category_list.html', {'category_list': cat_list})


@login_required(login_url='/')
def CategoryDelete(request,category_id):
    category_rec=Category.objects.filter(id=category_id)
    if category_rec:
        try:
            category_rec.delete()
            messages.success(request, 'Category deleted successfully')
        except:
            messages.warning(request, 'You can not delete the Category as its relation exists!')
    return redirect('/category_list/')


@login_required(login_url='/')
def Maker(request):
    if request.POST:
        form=maker_form(request.POST)
        form.save()
    else:
        form =maker_form()
    return render(request, 'maker.html',{'form':form})

@login_required(login_url='/')
def TyreList(request):
    tyre_all_list=Tyre.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(tyre_all_list, 10)
    try:
        tyre_list = paginator.page(page)
    except PageNotAnInteger:
        tyre_list = paginator.page(1)
    except EmptyPage:
        tyre_list = paginator.page(paginator.num_pages)
    path = 'http://'+request.META['HTTP_HOST']+'/media/'
    return render(request, 'tyre_list.html', {'tyre_list':tyre_list,'path':path})

@login_required(login_url='/')
def TyreImport(request):
    print 'within tyre import'
    if request.method == 'POST':
        tyre_resource = TyreResource()
        dataset = Dataset()
        tyre_recs = request.FILES['excel']

        imported_data = dataset.load(tyre_recs.read())
        for file_rec in imported_data.dict:
            if (Tyre.objects.filter(name=file_rec['Name']).exists()):
                continue
            else:
                tyre_rec=Tyre()
                vehicle_data=Vehicle.objects.filter(name=file_rec['vehicle'])
                if vehicle_data:
                    tyre_rec.vehicle=vehicle_data[0]
                category_data=Category.objects.filter(name=file_rec['category'])
                if category_data:
                    tyre_rec.category=category_data[0]
                tyre_rec.product_type=file_rec['Product Type']
                tyre_rec.normalsectionwidth=file_rec['Normal Section Width']
                tyre_rec.normalaspectratio=file_rec['Normal Aspect Ratio']
                tyre_rec.constructiontype=file_rec['Construction Type']
                tyre_rec.rimdiamter=file_rec['Rimdiamter']
                tyre_rec.loadindex=file_rec['Loadindex']
                tyre_rec.speedsymbol=file_rec['Speedsymbol']
                tyre_rec.pattern=file_rec['Pattern']
                tyre_rec.description=file_rec['Description']
                tyre_rec.warranty=file_rec['warranty']
                tyre_rec.warranty_summery=file_rec['warranty_summery']
                tyre_rec.mrp=file_rec['MRP']
                tyre_rec.construction_type_R=file_rec['construction_type_R']
                tyre_rec.name=file_rec['Name']
                tyre_rec.brand=file_rec['Brand']
                tyre_rec.save()
    return redirect('/tyre_list/')

@login_required(login_url='/')
def TyreImportData(request):
    tyre_resource = TyreResource()
    dataset =tyre_resource.export()
    header=Dataset(dataset)
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="tyre_data.xls"'
    return response

@login_required(login_url='/')
def AddTyre(request):
    form = tyre_form()
    return render(request, 'add_tyre.html', {'form': form})


@login_required(login_url='/')
def DeleteTyre(request,tyre_id):
    tyre_rec = Tyre.objects.filter(id=tyre_id)
    if tyre_rec:
        try:
            tyre_rec.delete()
            messages.success(request, 'Record deleted successfully')
        except:
            messages.warning(request, 'You can not delete the Tyre as its relation exists!')
    return redirect('/tyre_list/')

@login_required(login_url='/')
def TyreImportExcelFormat(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="tyre_import_format.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Tyres')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Name', 'Brand', 'Product Type', 'Normal Section Width', 'Normal Aspect Ratio','Construction Type','Rimdiamter',
               'Loadindex','Speedsymbol','Pattern','Description','warranty','warranty_summery','MRP','construction_type_R','vehicle','category']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    wb.save(response)
    return response
