from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=256,null=False)
    email=models.EmailField(null=False)
    role=models.CharField(max_length=20,null=False)
    password=models.CharField(max_length=20,null=False)


class Buisness_owner(models.Model):
    name=models.CharField(max_length=256,null=False)
    email=models.EmailField(null=False)
    password=models.CharField(max_length=20,null=False)
    upi_Id=models.CharField(max_length=50,null=False)

class Parking_lot(models.Model):
    location=models.CharField(max_length=256,null=False)
    name=models.CharField(max_length=256,null=False)
    length=models.FloatField(max_length=20,null=False)
    width=models.FloatField(max_length=20,null=False)
    Buisness_Id=models.IntegerField(max_length=20,null=False)

class Booking_info(models.Model):
    slot_row=models.IntegerField(null=False)
    slot_column=models.IntegerField(null=False)
    start_time=models.DateTimeField(auto_now_add=True)
    end_time=models.DateTimeField()
    car_no=models.CharField(max_length=20,null=False)
    payment=models.FloatField(null=False)
    customer_Id=models.IntegerField(max_length=20,null=False)
    parking_Id=models.IntegerField(max_length=20,null=False)
    

class camera(models.Model):
    type=models.CharField(max_length=256,null=False)
    parking_Id=models.IntegerField(null=False)

class slots(models.Model):
    type=models.CharField(null=False)
    slotrow=models.CharField(null=False)
    slotcolumn=models.CharField(null=False)
    parking_id=models.IntegerField()    
