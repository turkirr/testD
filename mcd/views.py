from django.shortcuts import render
from .models import *
# from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'mcd/index.html',{'name':'Turki', 'age':'15'})

def brands(request):
    return render(request, 'device/brands.html', {'brand': Brand.objects.all()})


def addbrand(request):
    return render(request, 'device/addbrand.html')


def device_type(request):
    return render(request, 'device/device_type.html',{'device_type': Device_Type.objects.all()})


def adddevice_type(request):
    return render(request, 'device/adddevice_type.html')


def devices(request):
    return render(request, 'device/brands.html', {'devices': Device.objects.all()})

def adddevice(request):
    return render(request, 'device/brands.html',)

def employee_devices(request):
    return render(request, 'device/employee_devices.html', {'employee_devices': Device.objects.all()})

def addemployee_device(request):
    return render(request, 'device/addemployee_devices.html',)

