from django.contrib import admin

# Register your models here.
from DirectoryService.models import servicelist

#class servicelist_admin(admin.ModelAdmin):
    
class servicelist_admin(admin.ModelAdmin):
    list_display = ('id','name','address','port','version')
    list_filter = ['id','name','address','port','version']
    

admin.site.register(servicelist,servicelist_admin)
