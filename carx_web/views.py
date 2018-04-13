# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, render_to_response

from . forms import loginForm
from django.contrib.auth import logout,login
# Create your views here.
from django.contrib import messages


def dashboard(request):
    return render(request, 'carx_web/dashboard.html')


def login(request):
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
            return redirect('/home/')
        else:
            messages.success(request, "Enter Valid User Name and Password.")
            return redirect('/carx/login/')

    return render(request, 'carx_login.html', {'form':form})


def logout(request):
    logout(request)
    return redirect('/carx/login/')


def create_vehicle(request):

    return render(request,  'carx_web/createVehicle.html')