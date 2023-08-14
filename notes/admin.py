from django.contrib import admin


# Register your models here.
from .models import Plant_1,Shop_1,Line_1,Machines,shift_1_count


class Plant_details(admin.ModelAdmin):
    list_display = ('plant_name','plant_location','plant_number')
    # readonly_fields = ['img_preview']

class Shop_details(admin.ModelAdmin):
    list_display = ('shop_name','shop_number','shop_in_which_plant')

class line_details(admin.ModelAdmin):
    list_display = ('line_name','line_number','line_in_which_shop')
    search_fields = ('line_name','line_in_which_shop',)
    

class machine_details(admin.ModelAdmin):
    list_display = ('machine_name','machine_number','machine_in_which_line','ok_count','ng_count','Total_count','shift_1_ok_count','shift_1_ng_count','shift_2_ok_count','shift_2_ng_count','Quality','last_date_updated')
    # list_filter = ("shift_1_ok_count" ,)
    search_fields = ('machine_name','machine_number',)

    def Total_count(self, obj):
         
        if obj.ok_count >= 0 and obj.ng_count >=0:
            return obj.ok_count+ obj.ng_count

    def Quality(self, obj):
        Quality = 0
        try:
            if obj.ok_count >= 0 and obj.ng_count >=0:
                Quality = ( obj.ok_count/ (obj.ok_count+ obj.ng_count) )*100
                Quality =round(Quality, 2)
        except:
            Quality = 0
        return Quality

    




admin.site.register(Plant_1,Plant_details)
admin.site.register(Shop_1,Shop_details)
admin.site.register(Line_1,line_details)
admin.site.register(Machines,machine_details)
