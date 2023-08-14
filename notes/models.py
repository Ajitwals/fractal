from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Plant_1(models.Model):
    plant_name = models.TextField(default = None,unique = True)
    plant_location = models.TextField(default = None)
    plant_number = models.IntegerField(default = 1)

    def __str__(self):
        return self.plant_name

class Shop_1(models.Model):
    shop_name = models.TextField(default = None,unique = True)
    shop_number = models.IntegerField(default = 1)
    shop_in_which_plant = models.ForeignKey(Plant_1,on_delete=models.CASCADE)

    def __str__(self):
        return self.shop_name

class Line_1(models.Model):
    line_name = models.TextField(default = None,unique = True)
    line_number = models.IntegerField(default = 1)
    line_in_which_shop = models.ForeignKey(Shop_1,on_delete=models.CASCADE)

    def __str__(self):
        return self.line_name

class Machines(models.Model):
    machine_name =  models.TextField(default = None)
    machine_number = models.IntegerField(unique = True)
    machine_in_which_line = models.ForeignKey(Line_1,on_delete=models.CASCADE)
    ok_count = models.IntegerField(default =0)
    ng_count = models.IntegerField(default = 0)
    last_date_updated = models.DateTimeField(auto_now_add=False,auto_created=True)


    shift_1_ok_count = models.IntegerField(default =0)
    shift_1_ng_count = models.IntegerField(default =0)
    shift_2_ok_count = models.IntegerField(default =0)
    shift_2_ng_count = models.IntegerField(default =0)


    def __str__(self):
        return self.machine_name


class shift_1_count(models.Model):
    machine_number = models.ForeignKey(Machines,on_delete=models.CASCADE)
    data = Machines.objects.all()



# combined 

