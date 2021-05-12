from django.contrib import admin
from models import Studio
from common.admin_ex import field
# Register your models here.

class StudioAdmin(admin.ModelAdmin):
    list_display=['get_name','logo']
    # list_display_links = ('name',)
    class Media:
        js = ('js/cus_add_studio_button.js',
        )    
    readonly_fields=['get_name']
    
    @field('name',allow_tags=True,admin_order_field='name')
    def get_name(self,obj):
        return '<a href="/studio/edit/{pk}">{name}</a>'.format(pk=obj.pk,name=obj.name)
    
admin.site.register(Studio, StudioAdmin)