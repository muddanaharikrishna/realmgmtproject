from django.db import models
#from django.core.urlresolvers import reverse   -- django - 1.11.17
from django.urls import reverse         #-- django - 3.0

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=64)
    father=models.CharField(max_length=64)
    dob=models.DateField()
    Occupation=models.CharField(max_length=64)
    mailid=models.EmailField()

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class Company(models.Model):
    name=models.CharField(max_length=64)
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('companydetail',kwargs={'pk':self.pk})

class Blockname(models.Model):
    name=models.CharField(max_length=64)
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('blockdetail',kwargs={'pk':self.pk})

class Floors(models.Model):
    name=models.CharField(max_length=64)
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('floordetail',kwargs={'pk':self.pk})

class Unit(models.Model):
#    verbose_name_plural='units'
    name=models.CharField(max_length=64)
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('unitdetail',kwargs={'pk':self.pk})

class Facing(models.Model):
    name=models.CharField(max_length=64)
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('facingdetail',kwargs={'pk':self.pk})

class UnitCreation(models.Model):
    STATUS_CHOICES=(('available','Available'),('sold','Sold'),('reserved','Reserved'),('registered','Registered'))
    flatno=models.IntegerField()
    cname=models.ForeignKey(Company,on_delete=models.CASCADE)
    bname=models.ForeignKey(Blockname,on_delete=models.CASCADE)
    floorno=models.ForeignKey(Floors,on_delete=models.CASCADE)
    unitno=models.ForeignKey(Unit,on_delete=models.CASCADE)
    face=models.ForeignKey(Facing,on_delete=models.CASCADE)
    status=models.CharField(max_length=11,choices=STATUS_CHOICES,default='available')

    def __str__(self):
        return str(self.cname)

    def __str__(self):
        return str(self.bname)

    def __str__(self):
        return str(self.floorno)

    def __str__(self):
        return str(self.unitno)

    def __str__(self):
        return str(self.face)

    def get_absolute_url(self):
        return reverse('unitcreationdetail',kwargs={'pk':self.pk})

class Amenities(models.Model):
    name=models.CharField(max_length=64)
    cost=models.FloatField()

    def get_absolute_url(self):
        return reverse('amenitiesdetail',kwargs={'pk':self.pk})

class UnitType(models.Model):
    name=models.CharField(max_length=64)

    def get_absolute_url(self):
        return reverse('unittypedetail',kwargs={'pk':self.pk})

"""class FlatCreation(models.Model):
    flatnumber=models.CharField(max_length=10)
    unit=models.ForeignKey(Unit)

    def __str__(self):
        return self.flatnumber
"""
