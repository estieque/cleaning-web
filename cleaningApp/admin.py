from django.contrib import admin

from cleaningApp.models import SiteSetting, Apointment

# Register your models here.

admin.site.register(SiteSetting)

class ApointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'service', 'member', 'add_date')

admin.site.register(Apointment, ApointmentAdmin)