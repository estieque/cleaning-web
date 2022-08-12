from django.contrib import admin

from contactApp.models import EmailSub

# Register your models here.

class EmailSubAdmin(admin.ModelAdmin):
    list_display = ('email', 'add_date')


admin.site.register(EmailSub, EmailSubAdmin)