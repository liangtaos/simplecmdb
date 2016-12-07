from django.contrib import admin
from hostinfo.models import Host, HostGroup



class HostAdmin(admin.ModelAdmin):
    list_display = [
               'hostname',
               'ip',
               'cpu_model',
               'cpu_num',
               'memory',
               'vendor',
               'product',
               'osver',
               'sn'


]
class HostGroupAdmin(admin.ModelAdmin):
    list_display = ['groupname']
admin.site.register(Host, HostAdmin)
admin.site.register(HostGroup, HostGroupAdmin)


