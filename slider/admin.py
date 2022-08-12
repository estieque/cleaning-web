from django.contrib import admin

from slider.models import *

# Register your models here.
class homeSliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    search_fields = ('name',)
    
admin.site.register(homeSlider, homeSliderAdmin)

class aboutSliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    search_fields = ('name',)
    
admin.site.register(aboutSlider, aboutSliderAdmin)

class blogSliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    search_fields = ('name',)
    
admin.site.register(blogSlider, blogSliderAdmin)

class portfolioSliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    search_fields = ('name',)
    
admin.site.register(portfolioSlider, portfolioSliderAdmin)

class contactSliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    search_fields = ('name',)
    
admin.site.register(contactSlider, contactSliderAdmin)