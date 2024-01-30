from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    
    # Brands
    path('brands',views.brands,),
    path('addbrand',views.addbrand,),
    
    # Devices
    path('devices',views.devices,),
    path('adddevice',views.adddevice,),
    
    # Device Type
    path('device_type',views.device_type,),
    path('adddevicetype',views.adddevice_type,),
    
    # Employees device
    path('employee_device',views.employee_devices,),
    path('addemployee_device',views.addemployee_device,),

    # MCD Mobile
    path('mobile',views.brands,),
    path('addmobile',views.addbrand,),

    # MCD Data
    path('data',views.brands,),
    path('adddata',views.addbrand,),

]
