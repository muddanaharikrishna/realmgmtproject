from django.contrib import admin
from customerapp.models import Customer, Company, Blockname, Floors, Unit, Facing, UnitCreation, Amenities # FlatCreation


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=['name','father','dob','Occupation','mailid']

admin.site.register(Customer,CustomerAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Company,CompanyAdmin)

class BlocknameAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Blockname,BlocknameAdmin)

class FloorsAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Floors,FloorsAdmin)

class UnitAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Unit,UnitAdmin)

class FacingAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Facing,FacingAdmin)

class UnitCreationAdmin(admin.ModelAdmin):
    list_display=['flatno','cname','bname','floorno','unitno','face','status']

admin.site.register(UnitCreation,UnitCreationAdmin)

class AmenitiesAdmin(admin.ModelAdmin):
    list_display=['name','cost']

admin.site.register(Amenities,AmenitiesAdmin)

"""class FlatCreationAdmin(admin.ModelAdmin):
    list_display=['flatnumber','unit']
admin.site.register(FlatCreation,FlatCreationAdmin)
"""
