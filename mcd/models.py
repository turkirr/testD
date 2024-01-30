from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)

class Device_Type(models.Model):
    name = models.CharField(max_length=50)

class Employees(models.Model):
    employee_id = models.CharField(primary_key = True, null = False, max_length=50)
    employee_name_full = models.CharField(null = False, max_length=400)
    grade = models.CharField(max_length=25, blank= True, null= True)
    position = models.CharField(null = True, blank = True, max_length=400)
    employee_department = models.CharField(max_length=400)

class Device(models.Model):
    brand_id=models.ForeignKey(Brand, on_delete = models.PROTECT)
    device_type_id=models.ForeignKey(Device_Type, on_delete = models.PROTECT)
    model = models.CharField(max_length=50)
    device_serial =models.CharField(max_length=30)
    receipt_number = models.CharField(max_length=30)
    cleared = models.CharField(default = '0' ,max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    device_status = models.CharField(max_length=30,)
    issue_date =models.DateTimeField()
    update_date =models.DateTimeField()

class Employee_Device(models.Model):
    device_id = models.ForeignKey(Device, on_delete = models.PROTECT)
    employee_id = models.ForeignKey(Employees, on_delete= models.CASCADE)
    request_number = models.CharField(max_length=30)
    receipt_number = models.CharField(max_length=30)
    receiving_status = models.CharField(max_length = 30)
    return_status = models.CharField(max_length = 30)
    issue_date = models.DateTimeField()
    update_date = models.DateTimeField()


class Mcd_Mobile(models.Model):
    employee_id = models.ForeignKey(Employees,null = False, on_delete= models.CASCADE)
    account_number = models.CharField(null = False, max_length=50)
    sim_serial_number = models.CharField(null = False,max_length=50)
    mobile_number = models.CharField(null = False, max_length=9)
    short_code = models.CharField(null = False, max_length=10)
    cleared = models.CharField(max_length=10)
    display_name = models.CharField(max_length=100)
    current_id = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    package = models.CharField(max_length=10)
    payment_value = models.CharField(max_length=30)
    PUK = models.CharField(max_length=30)
    PIN = models.CharField(max_length=30)
    request_number = models.CharField(max_length=20)
    comments = models.CharField(max_length=100)
    issue_date = models.DateTimeField()
    update_date = models.DateTimeField()

class Mcd_Data(models.Model):
    employee_id = models.ForeignKey(Employees,null = False, on_delete= models.CASCADE)
    account_number = models.CharField(null = False, max_length=50)
    sim_serial_number = models.CharField(null = False,max_length=50)
    service_number = models.CharField(null = False, max_length=12)
    short_code = models.CharField(max_length=10)
    cleared = models.CharField(max_length=10)
    display_name = models.CharField(max_length=100)
    current_id = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    package = models.CharField(max_length=10)
    payment_value = models.CharField(max_length=30)
    PUK = models.CharField(max_length=30)
    PIN = models.CharField(max_length=30)
    request_number = models.CharField(max_length=20)
    comments = models.CharField(max_length=100)
    issue_date = models.DateTimeField()
    update_date = models.DateTimeField()