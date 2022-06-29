from django.contrib import admin
from .models import ProbeList,ProbeModelDetail
# Register your models here.

class Probes(admin.ModelAdmin):
    list_display = ('ProbeID','ModelID','Status','CreateDate','Note')
    search_fields = ('ModelID','Status','CreateDate','Note')

class ProbeModelDetails(admin.ModelAdmin):
    list_display = ('id','ModelName','PortCount','CPU','Memony','HDD','Provider','Note')
    search_fields = ('ModelName','PortCount','CPU','Memony','HDD','Provider','Note')

admin.site.register(ProbeList, Probes)
admin.site.register(ProbeModelDetail, ProbeModelDetails)
