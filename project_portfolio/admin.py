from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from project_portfolio.models import Portfolio
# Register your models here.
class PortfolioAdmin(SummernoteModelAdmin):
    list_display = ('title','image_tag',)
    search_fields = ('title',)
    
    
admin.site.register(Portfolio, PortfolioAdmin)
    