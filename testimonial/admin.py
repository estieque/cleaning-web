from django.contrib import admin

from testimonial.models import Testimonial

# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'image_tag', 'email')
    
admin.site.register(Testimonial, TestimonialAdmin)