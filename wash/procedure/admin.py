from django.contrib import admin

# Register your models here.

from procedure.models import order
from procedure.models import WMODE
from procedure.models import LMODE
from procedure.models import FMODE
from procedure.models import CLIST
from procedure.models import delivery
from procedure.models import shop
from procedure.models import bag
from procedure.models import lock

class CLISTadmin(admin.ModelAdmin):
    list_display=('id','ORDID','WMODE','LMODE','FMODE','BAGNUM','TIME','PRICE',)
    list_filter=('id',)
    ordering=('id',)
admin.site.register(CLIST, CLISTadmin)

class WMODEadmin(admin.ModelAdmin):
    list_display=('id','WMODE','MONEY','POINTS','MEMISSIONS','TIME',)
    list_filter=('id',)
    ordering=('id',)
admin.site.register(WMODE, WMODEadmin)

class LMODEadmin(admin.ModelAdmin):
    list_display=('id','LMODE','MONEY','POINTS','MEMISSIONS','TIME',)
    list_filter=('id',)
    ordering=('id',)
admin.site.register(LMODE, LMODEadmin)

class FMODEadmin(admin.ModelAdmin):
    list_display=('id','FMODE','MONEY','POINTS','MEMISSIONS','TIME',)
    list_filter=('id',)
    ordering=('id',)
admin.site.register(FMODE, FMODEadmin)

class DELIVERYadmin(admin.ModelAdmin):
    list_display=('id','ORDID','SHOPID','PHONE','ADDRESS','GDATE',)
    list_filter=('id',)
    ordering=('id',)
admin.site.register(delivery, DELIVERYadmin)

admin.site.register(order)
admin.site.register(shop)
admin.site.register(bag)
admin.site.register(lock)
