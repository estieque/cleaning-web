from django.contrib import admin

# Register your models here.
from django_summernote.models import Attachment

admin.site.unregister(Attachment)