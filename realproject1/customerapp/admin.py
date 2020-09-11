from django.contrib import admin
from customerapp.models import Customer, Company, Blockname, Floors, Unit, Facing, UnitCreation, Amenities, UnitType, Scheme, UnitCosting # FlatCreation


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

class UnitTypeAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(UnitType,UnitTypeAdmin)

class SchemeAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Scheme,SchemeAdmin)

class UnitCostingAdmin(admin.ModelAdmin):
    list_display=['flatno','cname','bookingdate','schemetype','sft','face','unittype','price','pcharge','grossprice','discount','netprice','amenities']

admin.site.register(UnitCosting,UnitCostingAdmin)


"""class FlatCreationAdmin(admin.ModelAdmin):
    list_display=['flatnumber','unit']
admin.site.register(FlatCreation,FlatCreationAdmin)
"""
